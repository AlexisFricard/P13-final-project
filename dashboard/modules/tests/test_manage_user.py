"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User

from frontpage.tests.constants import ADMIN, STUDENT
from dashboard.modules.manage_user import add_user, mod_user


class AddUserTest(TestCase):
    def test_add_user_empty_field(self):

        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'firstname': '',
            'lastname': '',
            'email': '',

        }

        response = add_user(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout de l\'utilisateur'

    def test_add_user_not_same_email(self):

        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'firstname': 'xx',
            'lastname': 'xx',
            'email': 'xx',
            'emailconfirm': 'yy'
        }

        response = add_user(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout de l\'utilisateur'

    def test_add_user(self):

        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'firstname': 'test',
            'lastname': 'user',
            'email': 'xxx',
            'emailconfirm': 'xxx',
            'is_staff': 'on'
        }

        response = add_user(request)

        assert response['error'] is True
        assert response['text'] == (
            'Utilisateur ajouté\nEchec de l\'envoie du mail'
        )

        User.objects.get(username='testuser').delete()


class ModUserTest(TestCase):
    def test_mod_user_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'
        response = mod_user(request)
        assert response['error'] is True
        assert response['text'] == 'L\'utilisateur est introuvable'

    def test_mod_user_changes_fields(self):
        # Change response
        user = STUDENT
        request = RequestFactory().get(f'mod_data?id={user.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
                'email': 'y',
                'username': 'testmoduser',
                'is_staff': 'on'
            }

        response = mod_user(request)

        assert response['error'] is True
        assert response['text'] == (
            'Élément modifié\nEchec de l\'envoie du mail'
        )

    def test_mod_user_changes_staff(self):
        user = STUDENT
        user.is_staff = True
        user.save()
        request = RequestFactory().get(f'mod_data?id={user.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
                'email': 'y',
                'username': 'testmoduser',
                'is_staff': None,
            }

        response = mod_user(request)

        assert response['error'] is True
        assert response['text'] == (
            'Élément modifié\nEchec de l\'envoie du mail'
        )

    def test_mod_user_changes_from_student(self):

        user = STUDENT
        request = RequestFactory().get(f'mod_data?id={user.id}')
        request.user = STUDENT
        request.method = 'POST'
        request.POST = {
                'email': 'testmoduser',
                'username': 'testmoduser2',
                'name_': 'xxx',
            }

        response = mod_user(request)

        assert response['error'] is False
