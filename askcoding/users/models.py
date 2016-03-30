# -*- coding: utf-8 -*-

# Third Party
from askcoding.base.models import UUIDModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        is_active = extra_fields.pop('is_active', True)  # Change this setting to change default behaviour of user
        user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, **extra_fields)
        if password is None:
            user.set_unusable_password()
        else:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
    name = models.CharField('Full Name', max_length=255, blank=True)
    email = models.EmailField('email address', unique=True, db_index=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')

    receive_emails = models.BooleanField(default=False, verbose_name='Receive Marketing Emails')

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('-date_joined', )

    def __str__(self):
        return str(self.email)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name.strip()
