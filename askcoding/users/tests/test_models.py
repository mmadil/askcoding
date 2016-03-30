# -*- coding: utf-8 -*-

# Third Party
import pytest
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db
User = get_user_model()


def test_create_user():
    u = User.objects.create_user(email='f@example.com', password='abc', name="test user")
    assert u.is_active is True
    assert u.is_staff is False
    assert u.is_superuser is False
    assert u.email == 'f@example.com'
    assert str(u) == str(u.email)
    assert u.get_short_name() == 'test user'


def test_create_user_with_unusable_password():
    u = User.objects.create_user(email='f@example.com')
    assert u.has_usable_password() is False


def test_create_super_user():
    u = User.objects.create_superuser(email='f@example.com', password='abc')
    assert u.is_active is True
    assert u.is_staff is True
    assert u.is_superuser is True
    assert str(u) == str(u.email)
