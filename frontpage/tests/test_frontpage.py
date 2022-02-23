# ===========================
# ===== FRONTPAGE ======
# ===========================

# asgi to test localy
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.views import (
    index, actualities, actuality,
)

from .constants import ANONYMOUS
from .tools import create_actuality


def test_view_index():

    request = RequestFactory().get("")

    view = index(request)
    assert view.status_code == 200

    request.COOKIES = {'cookie_accord': True}
    actu = create_actuality('actu1')
    actu2 = create_actuality('actu2')
    actu3 = create_actuality('actu3')
    actu4 = create_actuality('actu4')

    view = index(request)
    assert view.status_code == 200

    actu.delete()
    actu2.delete()
    actu3.delete()
    actu4.delete()


def test_actualities():
    actu = create_actuality()
    request = RequestFactory().get("/actualités")
    request.user = ANONYMOUS

    view = actualities(request)

    assert view.status_code == 200
    actu.delete()


def test_actuality():

    request = RequestFactory().get("/actualité?id=0")
    view = actuality(request)

    assert view.status_code == 302

    actu = create_actuality()
    request = RequestFactory().get(
        f"/actualité?id={actu.id}"
        )
    view = actuality(request)
    assert view.status_code == 200

    actu.delete()
