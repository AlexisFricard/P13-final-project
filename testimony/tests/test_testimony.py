from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ANONYMOUS
from testimony.views import after
from testimony.models import Testimony


def test_testimony():
    testi = Testimony.objects.create(
        text='aaa #bbb',
        author='test',
        promotion='test',
        job="test",
        sector='test'
    )
    request = RequestFactory().get("et-après")
    request.user = ANONYMOUS

    view = after(request)

    assert view.status_code == 200

    testi.delete()
