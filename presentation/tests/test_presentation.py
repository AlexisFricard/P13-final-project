from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ANONYMOUS
from presentation.views import presentation_page
from frontpage.tests.tools import create_member


def test_presentation():
    request = RequestFactory().get("présentation")
    request.user = ANONYMOUS
    membdirec = create_member('team', 'director')
    membstaff = create_member('team', 'staff')

    view = presentation_page(request)

    assert view.status_code == 200

    membdirec.delete()
    membstaff.delete()
