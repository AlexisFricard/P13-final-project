"""
Association file test
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ANONYMOUS
from association.views import association
from association.models import MemberOffice


def test_association():

    request = RequestFactory().get("")
    request.user = ANONYMOUS

    view = association(request)

    pres = MemberOffice.objects.create(
        name="testpres",
        link='formationtest',
        img_link='2022test',
        genre='f',
        promotion='xxx',
        role='president'
    )
    vice = MemberOffice.objects.create(
        name="testvice",
        link='formationtest',
        img_link='2022test',
        genre='f',
        promotion='xxx',
        role='vice'
    )
    secre = MemberOffice.objects.create(
        name="testsecret",
        link='formationtest',
        img_link='2022test',
        genre='f',
        promotion='xxx',
        role='secretary'
    )
    treasu = MemberOffice.objects.create(
        name="testtreas",
        link='formationtest',
        img_link='2022test',
        genre='f',
        promotion='xxx',
        role='treasurer'
    )
    request = RequestFactory().get("")
    request.user = ANONYMOUS

    view = association(request)

    assert view.status_code == 200

    pres.delete()
    vice.delete()
    secre.delete()
    treasu.delete()
