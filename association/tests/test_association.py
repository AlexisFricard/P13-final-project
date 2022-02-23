"""
Association file test
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.middleware import SessionMiddleware
from frontpage.tests.constants import ANONYMOUS
from association.views import association
from association.models import MemberOffice


def test_association():

    try:
        MemberOffice.objects.get(role='president')
        pres = False
    except ObjectDoesNotExist:
        pres = MemberOffice.objects.create(
            name="testpres",
            link='formationtest',
            img_link='2022test',
            genre='f',
            promotion='xxx',
            role='president'
        )
    
    try:
        MemberOffice.objects.get(role='vice')
        vice = False
    except ObjectDoesNotExist:
        vice = MemberOffice.objects.create(
            name="testvice",
            link='formationtest',
            img_link='2022test',
            genre='f',
            promotion='xxx',
            role='vice'
        )
    
    try:
        MemberOffice.objects.get(role='secretary')
        secre = False
    except ObjectDoesNotExist:
        secre = MemberOffice.objects.create(
            name="testsecret",
            link='formationtest',
            img_link='2022test',
            genre='f',
            promotion='xxx',
            role='secretary'
        )
    
    try:
        MemberOffice.objects.get(role='treasurer')
        treasu = False
    except ObjectDoesNotExist:
        treasu = MemberOffice.objects.create(
            name="testtreas",
            link='formationtest',
            img_link='2022test',
            genre='f',
            promotion='xxx',
            role='treasurer'
        )

    request = RequestFactory().get("/association")
    request.user = ANONYMOUS
    request.method = 'GET'
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    view = association(request)

    assert view.status_code == 200

    if pres:
        pres.delete()
    if vice:
        vice.delete()
    if secre:
        secre.delete()
    if treasu:
        treasu.delete()
