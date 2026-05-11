from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Category, Product, Order
from api.serializers import (
    CategorySerializer, ProductSerializer, OrderSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve food categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve products. Filter by category with ?category=<id>."""
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category_id=category)
        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(name__icontains=search)
        return qs

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Return featured products for the homepage."""
        featured = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    """Create and retrieve orders."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def perform_create(self, serializer):
        # Save the order first
        order = serializer.save()
        
        # Import task here to avoid circular imports if any
        from api.tasks import send_order_confirmation_email
        
        # Trigger the background task to send the email
        send_order_confirmation_email.delay(order.id)
