""" CONSTANTS FOR TESTS """
from django.contrib.auth.models import AnonymousUser

from .tools import create_user, initialize_user


initialize_user()

ADMIN = create_user('admin')
STUDENT = create_user('student')
ANONYMOUS = AnonymousUser()
