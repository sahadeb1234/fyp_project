from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from .models import Order, Customer


class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )


password_reset_token = MyPasswordResetTokenGenerator()
