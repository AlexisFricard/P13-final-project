
"""
Discussion test
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ADMIN
from chat.views import room


def test_chat():
    request = RequestFactory().get("/discussion/publique")
    request.user = ADMIN
    request.method = 'GET'
    view = room(request, 'publique')

    assert view.status_code == 200
