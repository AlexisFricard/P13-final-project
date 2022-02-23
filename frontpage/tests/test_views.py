# asgi to test localy
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.views import (
    setcookie,
    error_400, error_403, error_404, error_500
)


# ===================
# ===== COOKIE ======
# ===================
class CookieTest(TestCase):
    def test_setcookie(self):
        request = RequestFactory()
        response = setcookie(request)
        assert response.status_code == 200


# ===================
# ===== ERRORS ======
# ===================
class TestError(TestCase):
    def test_400(self):
        request = RequestFactory().get("")
        view = error_400(request, "exception")
        assert view.status_code == 200

    def test_403(self):
        request = RequestFactory().get("")
        view = error_403(request, "exception")
        assert view.status_code == 200

    def test_404(self):
        request = RequestFactory().get("/test404")
        view = error_404(request, "exception")
        assert view.status_code == 200

    def test_500(self):
        request = RequestFactory().get("")
        view = error_500(request)
        assert view.status_code == 200
