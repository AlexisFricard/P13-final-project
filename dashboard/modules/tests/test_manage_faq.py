"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_faq
from collabspace.models import Faq

from dashboard.modules.manage_faq import add_faq, mod_faq


class AddFaqTest(TestCase):
    def test_add_faq_empty_question(self):

        # Empty question
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'faq',
            'question': "",
            'text': 'x',
        }

        response = add_faq(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout à la FAQs'

    def test_add_faq_empty_text(self):

        # Empty article
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'faq',
            'question': "test_add_data",
            'text': '',
        }

        response = add_faq(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout à la FAQs'

    def test_add_faq_error(self):
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'question': 1,
            'article': 'x'
        }
        response = add_faq(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout à la FAQs'

    def test_add_faq(self):
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'faq',
            'question': "questiontest",
            'text': 'text test',
        }
        response = add_faq(request)
        assert response['error'] is False
        assert response['text'] == 'La faq à été ajoutée'

        Faq.objects.get(question='questiontest').delete()


class ModFaqTest(TestCase):
    def test_mod_faq_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'

        response = mod_faq(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_faq_changes(self):
        # Change response
        faq = create_faq()
        request = RequestFactory().get(f'mod_data?id={faq.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'question': 'questiontest',
            'is_state': "0",
            'response': 'testxx',
        }

        response = mod_faq(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # Change question
        request.POST = {
            'question': 'questiontest2',
            'is_state': "on",
            'response': 'testxx',
        }

        response = mod_faq(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # Delete it
        request.POST = {
            'title': 'questiontest2',
            'is_state': "0",
            'question': 'testxx',
            'delete_it': 'on',
        }

        response = mod_faq(request)

        assert response['error'] is False
        assert response['text'] == 'Suppression terminé'

        faq.delete()
