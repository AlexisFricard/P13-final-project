"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.tests.tools import create_promotion
from dashboard.modules.manage_promotion import add_promotion, mod_promotion

PROMOTION = {
    'box': 'promotion',
    'img_link': "test",
    'formation': 'formationtest',
    'date': '2022test',
    'col1-title': 'xxx',
    'col2-title': 'xxx',
    'col3-title': 'xxx',
    'col1-student1-name': 'xxx',
    'col1-student1-target': 'xxx',
    'col1-student1-link': 'xxxx',
    'col2-student1-name': 'xxx',
    'col2-student1-target': 'xxx',
    'col2-student1-link': 'xxxx',
    'col3-student1-name': 'xxx',
    'col3-student1-target': 'xxx',
    'col3-student1-link': 'xxxx',
}


class AddPromotionTest(TestCase):
    def test_add_promotion_empty_field(self):

        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'img_link': "test",
            'formation': 'formationtest',
            'date': ''
        }
        response = add_promotion(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout de la promotion'

    def test_add_promotion(self):

        request = RequestFactory().get('')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = PROMOTION

        response = add_promotion(request)
        assert response['error'] is False
        assert response['text'] == 'La promotion à été ajoutée'


class ModOfficeTest(TestCase):
    def test_mod_promo_false_id(self):
        # False Id
        request = RequestFactory().get('mod_data?id=1651651')
        request.user = ADMIN
        request.method = 'POST'
        response = mod_promotion(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_promo(self):
        promo = create_promotion()

        request = RequestFactory().get(f'mod_data?id={promo.id}')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = PROMOTION

        response = mod_promotion(request)
        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        promo.delete()
