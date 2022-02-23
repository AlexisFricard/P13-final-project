# asgi to test localy
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import (
    create_actuality, create_member,
    create_testimony, create_user,
)
from dashboard.views import (
    dashboard, add_data, mod_data, delete_it
)


def test_dashboard():
    # Empty article
    request = RequestFactory().get('')
    request.user = ADMIN
    request.method = 'POST'

    member1 = create_member('team', 'director')
    member2 = create_member('team', 'staff')

    view = dashboard(request, 0)
    assert view.status_code == 200

    member1.delete()
    member2.delete()

    view = dashboard(request, 'home')
    assert view.status_code == 200


def test_add_data():

    list_of_dashboard = [
        '', 'actuality', 'faq', 'link',
        'testimony', 'promotion', 'user',
        'member'
    ]

    request = RequestFactory().get('')
    request.user = ADMIN
    request.method = 'POST'

    for box in list_of_dashboard:
        if box == 'member':
            # OFFICE
            request.POST = {
                'box': box,
                'box-2': 'office',
            }

            view = add_data(request)
            assert view.status_code == 302

            # TEAM
            request.POST = {
                'box': box,
                'box-2': 'team',
            }

            view = add_data(request)
            assert view.status_code == 302

        else:
            # OTHER
            request.POST = {
                'box': box,
            }

            view = add_data(request)
            assert view.status_code == 302


def test_mod_data():

    list_of_dashboard = [
        'actuality', 'faq',  'link',
        'testimony', 'promotion', 'user',
        'office', 'team',
        ]

    request = RequestFactory().get('')
    request.user = ADMIN
    request.method = 'POST'

    for box in list_of_dashboard:
        # OTHER
        request.GET = {
            'dbdata': box,
            'id': 0
        }

        view = mod_data(request)
        assert view.status_code == 302


def test_delete_it_empty_type():
    # list_of_type = ['actu', 'testi', 'office', 'team', 'user']

    request = RequestFactory().get('del_?id=1&t=test')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_from_user_account():

    request = RequestFactory().get('del_?id=1&t=test&username=test')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_actu():
    actu = create_actuality()

    request = RequestFactory().get(f'del_?id={actu.id}&t=actu')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_testimony():
    testi = create_testimony()
    request = RequestFactory().get(f'del_?id={testi.id}&t=testi')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_office():
    member = create_member('office', 'promotiontest')
    request = RequestFactory().get(f'del_?id={member.id}&t=office')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_team():
    member = create_member('team', 'promotiontest')
    request = RequestFactory().get(f'del_?id={member.id}&t=team')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302


def test_delete_it_user():
    member = create_user('student')
    request = RequestFactory().get(f'del_?id={member.id}&t=user')
    request.user = ADMIN

    view = delete_it(request)
    assert view.status_code == 302
