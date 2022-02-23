from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ANONYMOUS
from ourstudent.views import ourstudent
from frontpage.tests.tools import create_promotion


def test_ourstudent():
    promo = create_promotion()

    request = RequestFactory().get("nos-diplômés")
    request.user = ANONYMOUS

    view = ourstudent(request)
    assert view.status_code == 200

    promo.delete()
