from django.db import models
from models import emailauth

class EmailUserAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = emailauth.objects.get(email=username)
            if user.check_password(password):
                return user
        except emailauth.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = emailauth.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except E.DoesNotExist:
            return None
