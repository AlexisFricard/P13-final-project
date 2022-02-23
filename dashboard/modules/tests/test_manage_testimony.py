"""
Test testimony file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_testimony
from testimony.models import Testimony

from dashboard.modules.manage_testimony import add_testimony, mod_testimony


class AddTestiTest(TestCase):
    def test_add_testimony_empty_sector(self):

        # Empty article
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'testimony',
            'text': "test",
            'sector': '',
            'author': 'testauthor',
            'promotion': 'promotion test',
            'job': 'testjob',
        }

        response = add_testimony(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du témoignage'

    def test_add_testimony_error(self):
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'testimony',
            'text': "test",
            'sector': 'test',
            'author': 'testauthor',
            'promotion': 0,
        }

        response = add_testimony(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout du témoignage'

    def test_add_testimony(self):
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'testimony',
            'text': "test",
            'sector': 'sectortest',
            'author': 'testauthor',
            'promotion': 'promotion test',
            'job': 'testjob',
        }

        response = add_testimony(request)

        assert response['error'] is False
        assert response['text'] == 'Le témoignage à été ajouté'
        Testimony.objects.get(author='testauthor').delete()


class ModTestiTest(TestCase):
    def test_mod_testimony_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'

        response = mod_testimony(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_testimony_changes(self):
        # Change response
        testi = create_testimony()
        request = RequestFactory().get(f'mod_data?id={testi.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'is_state': "0",
            'box': 'testimony',
            'text': "test",
            'sector': 'sectortest',
            'author': 'testauthor',
            'promotion': 'promotion test',
            'job': 'testjob',
        }

        response = mod_testimony(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # Change author
        request.POST = {
            'is_state': "on",
            'box': 'testimony',
            'text': "test",
            'sector': 'sectortest',
            'author': 'testauthor',
            'promotion': 'promotion test',
            'job': 'testjob',
        }

        response = mod_testimony(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        testi.delete()
