# -*- coding: utf-8 -*-

# Third Party
import factory
from django.conf import settings
from django.utils.text import slugify


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    email = factory.lazy_attribute(lambda o: slugify(o.name)+'@example.com')
    name = factory.Faker('name')
    password = factory.PostGeneration(lambda obj, *args, **kwargs: obj.set_password('test'))
