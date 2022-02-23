"""
Test actuality file
"""
from mastercontrat import asgi  # noqa
from mastercontrat import wsgi  # noqa

from django.test import RequestFactory, TestCase

from frontpage.tests.constants import ADMIN
from frontpage.models import Actuality

from dashboard.modules.manage_actuality import add_actu, mod_actu

from frontpage.tests.tools import create_actuality

ACTU_ERROR = {
    'box': 'actuality',
    'title': "test_actu",
    'start': 'ERROR',
    'end': '2023-01-01',
    'article': 'x',
    'short_desc': 'x',
    # Link img
    'link': 'none',
    'link_ext': 'https://mockerror.fr',
    # Format for landscape or portrait
    'format': 'none',
    # Link to another website -> btn
    'ext_link': 'https://openclassrooms.com/'
}
ACTU_LINK_EXT_NO_FORMAT = {
    'box': 'actuality',
    'title': "test_actu_x",
    'start': '2023-01-01',
    'end': '2023-01-01',
    'article': 'x',
    'short_desc': 'x',
    # Link img
    'link': 'none',
    'link_ext': 'https://mockerror.fr',
    # Format for landscape or portrait
    'format': 'none',
    # Link to another website -> btn
    'ext_link': 'https://openclassrooms.com/'
}
ACTU_LINK_INT_FORMAT = {
    'box': 'actuality',
    'title': "test_actu_y",
    'start': '2022-01-01',
    'end': '2022-01-01',
    'article': 'y',
    'short_desc': 'y',
    # Link img
    'link': 'https://openclassrooms.com/',
    'link_ext': 'none',
    # Format for landscape or portrait
    'format': 'on',
    # Link to another website -> btn
    'ext_link': 0,
}


class AddActualityTest(TestCase):
    def test_add_actu_empty_title(self):

        # Empty title
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'actuality',
            'title': "",
            'article': 'x',
        }

        response = add_actu(request)
        assert response['error'] is True
        assert response['text'] == 'Le titre ou l\'article est vide'

    def test_add_actu_empty_article(self):

        # Empty article
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'actuality',
            'title': "test_add_data",
            'article': '',
        }

        response = add_actu(request)
        assert response['error'] is True
        assert response['text'] == 'Le titre ou l\'article est vide'

    def test_add_actu_error(self):
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = ACTU_ERROR
        response = add_actu(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de l\'ajout de l\'actualité'

    def test_add_actu_LIF(self):
        # Img link -> media file || ext_link -> no || format -> on
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = ACTU_LINK_INT_FORMAT

        response = add_actu(request)
        assert response['error'] is False
        assert response['text'] == 'L\'actualité à été ajoutée'

        Actuality.objects.get(title='test_actu_y').delete()

    def test_add_actu_LENF(self):
        # Img link -> media file || ext_link -> no || format -> on
        request = RequestFactory().get('add_data')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = ACTU_LINK_EXT_NO_FORMAT

        response = add_actu(request)
        assert response['error'] is False
        assert response['text'] == 'L\'actualité à été ajoutée'
        Actuality.objects.get(title='test_actu_x').delete()


class ModActualityTest(TestCase):
    def test_mod_actu_false_id(self):
        # False id
        request = RequestFactory().get('mod_data?id=9999')
        request.user = ADMIN
        request.method = 'POST'
        request.POST = {
            'box': 'actuality',
            'title': "test_add_data",
            'article': 'x',
        }

        response = mod_actu(request)
        assert response['error'] is True
        assert response['text'] == 'Echec de la modification'

    def test_mod_actu_changes(self):
        # Valide id
        actu = create_actuality()
        request = RequestFactory().get(f'mod_data?id={actu.id}')
        request.user = ADMIN
        request.method = 'POST'

        # TEST 1
        # Change :
        # Dates / Title / Start / End
        # state = 1 -> 0
        # ext_link = 0 -> link
        # img_link -> not exist

        request.POST = ACTU_LINK_EXT_NO_FORMAT
        response = mod_actu(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        actu = create_actuality()
        request = RequestFactory().get(f'mod_data?id={actu.id}')
        request.user = ADMIN
        request.method = 'POST'
        # TEST 2
        # Change :
        # Article / Short Desc
        # state = 0 -> 1
        # ext_link == actu.external_link
        # format = 0 -> 1
        actu.state = 0
        actu.save()
        ACTU_LINK_INT_FORMAT['is_state'] = 'on'
        ACTU_LINK_INT_FORMAT['ext_link'] = '0'

        request.POST = ACTU_LINK_INT_FORMAT
        response = mod_actu(request)

        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        # TEST 3
        # Change :
        # ext_link = actu.external_link(!0) -> 0
        # format = 1 -> 0
        actu.format, actu.external_link = 1, "test"
        actu.save()
        ACTU_LINK_INT_FORMAT['format'] = '0'
        request.POST = ACTU_LINK_INT_FORMAT

        response = mod_actu(request)
        assert response['error'] is False
        assert response['text'] == 'Élément modifié'

        actu.delete()
