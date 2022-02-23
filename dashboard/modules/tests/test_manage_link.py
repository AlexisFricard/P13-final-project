"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_link
from collabspace.models import Link

from dashboard.modules.manage_link import add_link, mod_link


class AddLinkTest(TestCase):
    def test_add_link_empty_title(self):

        # Empty question
        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'link',
            'title': "",
            'link': 'x',
        }

        response = add_link(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du lien'

    def test_add_link_empty_link(self):

        # Empty article
        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'link',
            'title': "test_add_data",
            'link': '',
        }

        response = add_link(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du lien'

    def test_add_link_error(self):
        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'title': None,
            'link': 'x'
        }
        response = add_link(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du lien'

    def test_add_link(self):
        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'link',
            'title': "linktest",
            'link': 'text test',
        }
        response = add_link(request)
        assert response['error'] is False
        assert response['text'] == 'Le lien à été ajouté'
        Link.objects.get(title='linktest').delete()


class ModLinkTest(TestCase):
    def test_mod_link_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'

        response = mod_link(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_link_changes(self):
        # Change response
        link = create_link()
        request = RequestFactory().get(f'mod_data?id={link.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'title': 'titletest',
            'is_state': "0",
            'link': 'tesstxx',
        }

        response = mod_link(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # Change title
        request.POST = {
            'title': 'titletest2',
            'is_state': "on",
            'link': 'testxx',
        }

        response = mod_link(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # Delete it
        request.POST = {
            'title': 'titletest2',
            'is_state': "0",
            'link': 'testxx',
            'delete_it': 'on',
        }

        response = mod_link(request)

        assert response['error'] is False
        assert response['text'] == 'Suppression terminé'

        link.delete()
