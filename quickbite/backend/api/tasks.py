from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order, OrderItem

@shared_task
def send_order_confirmation_email(order_id):
    """Task to send a detailed order confirmation email."""
    try:
        order = Order.objects.get(pk=order_id)
        items = order.items.all()
        
        # Format the items list
        items_list = ""
        for item in items:
            items_list += f"- {item.product_name} x {item.quantity} (${item.price})\n"
        
        subject = f'QuickBite - Order Confirmation #{order.id}'
        message = (
            f"Hi {order.customer_name},\n\n"
            f"Thank you for your order! We have received it and it is now being prepared.\n\n"
            f"Order Details:\n"
            f"------------------\n"
            f"{items_list}"
            f"------------------\n"
            f"Total Price: ${order.total_price}\n\n"
            f"Delivery Address:\n{order.customer_address}\n\n"
            f"We will notify you when your food is on the way!"
        )
        
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [order.customer_phone if '@' in order.customer_phone else 'bilaltareq2005@gmail.com'] # Falling back to verified email for sandbox
        
        # In a real app, you'd use a field for email. Let's assume customer_name or a new field if available.
        # For now, I'll send it to your verified email so you can see it.
        recipient_list = ['bilaltareq2005@gmail.com'] 
        
        send_mail(subject, message, email_from, recipient_list)
        return f"Email sent successfully for Order #{order_id}"
    except Order.DoesNotExist:
        return f"Order #{order_id} not found"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
