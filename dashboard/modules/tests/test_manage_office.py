"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_member

from dashboard.modules.manage_office import add_office, mod_office


class AddOfficeTest(TestCase):
    def test_add_office_member_empty_field(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'office',
            'name': '',
        }

        response = add_office(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du membre'

    def test_add_office_member_error(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'office',
            'name': "test",
            'link': 'formationtest',
            'img_link': '2022test',
            'genre': None,
            'promotion': 'xxx',
            'role': 'president'
        }

        response = add_office(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du membre'

    def test_add_office_member(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'office',
            'name': "test",
            'link': 'formationtest',
            'img_link': '2022test',
            'genre': 'f',
            'promotion': 'xxx',
            'role': 'president'
        }

        response = add_office(request)
        assert response['error'] is False
        assert response['text'] == 'Le membre à été ajouté'


class ModOfficeTest(TestCase):
    def test_mod_office_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'
        response = mod_office(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_office_changes(self):
        # Change response
        member = create_member('office', 'testmodoffice')
        request = RequestFactory().get(f'mod_data?id={member.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
                'name': "newname",
                'link': 'newlink',
                'img_link': 'newlink',
                'genre': 'f',
                'promotion': 'newpromotion',
                'role': 'newrole'
            }

        response = mod_office(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        member.delete()
