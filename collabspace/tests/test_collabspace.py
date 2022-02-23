# ===========================
# ====== STUDENT USER =======
# ===========================

# asgi to test localy
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

from collabspace.views import (
    myspace, myaccount, log_out, log_in
)

from frontpage.tests.constants import (
    STUDENT, ANONYMOUS
)
from frontpage.tests.tools import create_faq, create_link


def test_myspace():
    # Connected
    request = RequestFactory().get("")
    request.user = STUDENT

    faq = create_faq()
    link = create_link()

    view = myspace(request, '')
    assert view.status_code == 200

    view = myspace(request, 'home')
    assert view.status_code == 200

    faq.delete()
    link.delete()


def test_myaccount():

    request = RequestFactory().get("")
    request.user = STUDENT

    view = myaccount(request)

    assert view.status_code == 200


def test_log_out():

    request = RequestFactory().post("")
    request.user = STUDENT

    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    view = log_out(request)

    assert view.status_code == 302


def test_log_in():
    # Connect to
    request = RequestFactory().post("")
    request.user = ANONYMOUS
    request.POST = {
        'username': 'student',
        'password': 'azerty123'
    }

    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    view = log_in(request)
    assert view.status_code == 302

    # False password
    request.POST = {
        'username': 'student',
        'password': 'FALSEPASSWORD'
    }

    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    view = log_in(request)
    assert view.status_code == 302
