# -*- coding: utf-8 -*-

# Third Party
from django.core.urlresolvers import reverse


def test_home_file(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
