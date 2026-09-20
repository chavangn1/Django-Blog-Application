from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

from accounts.models import User
from accounts.tokens import account_activation_token


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if not created:
        return  # don't re-fire on every save (e.g. when we flip is_active later)

    uid = urlsafe_base64_encode(force_bytes(instance.pk))
    token = account_activation_token.make_token(instance)

    activation_link = f"{settings.APP_BASE_URL}/accounts/activate/{uid}/{token}/"

    message = render_to_string('accounts/activation_email.txt', {
        'full_name': instance.full_name,
        'activation_link': activation_link,
    })

    send_mail(
        subject="Activate your BlogHub account",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
        fail_silently=False,
    )