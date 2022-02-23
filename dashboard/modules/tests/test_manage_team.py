"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_member

from dashboard.modules.manage_team import add_team, mod_team


class AddTeamTest(TestCase):
    def test_add_team_member_empty_field(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'team',
            'name': '',
        }

        response = add_team(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du membre'

    def test_add_team_member_error(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'team',
            'name': "test",
            'link': 'formationtest',
            'img_link': '2022test',
            'status1': 1,
            'grade': 'vice',
        }

        response = add_team(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du membre'

    def test_add_team_member(self):

        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'team',
            'name': "test",
            'link': 'formationtest',
            'img_link': '2022test',
            'status1': 'prof',
            'status2': 'prof',
            'status3': 'prof',
            'status4': 'prof',
            'status5': 'prof',
            'grade': 'vice',
        }

        response = add_team(request)
        assert response['error'] is False
        assert response['text'] == 'Le membre à été ajouté'


class ModTeamTest(TestCase):
    def test_mod_team_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'
        response = mod_team(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_team_changes(self):
        # Change response
        member = create_member('team', 'testmodteam')
        request = RequestFactory().get(f'mod_data?id={member.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'member',
            'box-2': 'team',
            'name': "test",
            'link': 'formationtest',
            'img_link': '2022test',
            'status1': 'prof',
            'status2': 'prof',
            'status3': 'prof',
            'status4': 'prof',
            'status5': 'prof',
            'grade': 'vice',
        }

        response = mod_team(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'
