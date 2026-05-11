from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(order_id, customer_email, customer_name):
    """Task to send an order confirmation email."""
    subject = f'QuickBite - Order Confirmation #{order_id}'
    message = f'Hi {customer_name},\n\nThank you for your order! We have received it and it is now being prepared.\n\nOrder ID: #{order_id}'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]
    
    try:
        send_mail(subject, message, email_from, recipient_list)
        return f"Email sent successfully to {customer_email}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
