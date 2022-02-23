"""
ACTUALITY FILE
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from frontpage.models import Actuality

from modules.check_url import check_url

# TODO PROD SETTINGS
# from mastercontrat.settings import STATIC_URL
# TODO DEV SETTINGS:
from mastercontrat.dev_settings import STATIC_URL


@login_required
def add_actu(request):
    data = {}
    data['view'] = 'ajouter-une-actualité'
    if (request.POST.get('title') and
            request.POST.get('article')) != "":

        if request.POST.get('link') != 'none':
            link_img = request.POST.get('link')
        else:
            link_img = request.POST.get('link_ext')

        img_link = link_img
        if link_img:
            if link_img.startswith('https'):
                img_exist = check_url(link_img)
                if not img_exist:
                    img_link = STATIC_URL + "assets/img/bannerpalette/red.png"

        if request.POST.get('ext_link'):
            ext_link = request.POST.get('ext_link')
        else:
            ext_link = 0

        if request.POST.get('format') == "on":
            format_ = 1
        else:
            format_ = 0

        try:
            Actuality.objects.create(
                title=request.POST.get('title'),
                date=request.POST.get('start'),
                stop_date=request.POST.get('end'),
                article=request.POST.get('article'),
                short_desc=request.POST.get('short_desc'),
                img_title=img_link,
                format=format_,
                external_link=ext_link,
                state=1
            )
            data['error'] = False
            data['text'] = 'L\'actualité à été ajoutée'

        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout de l\'actualité'
    else:
        data['error'] = True
        data['text'] = 'Le titre ou l\'article est vide'

    return data


@login_required
def mod_actu(request):
    data = {}
    data['view'] = 'modifier-une-actualité'
    try:
        actu = Actuality.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        actu = None
    if actu:
        # Image
        if request.POST.get('link') != actu.img_title:
            img_exist = check_url(request.POST.get('link'))

            if img_exist:
                actu.img_link = request.POST.get('link')
            else:
                actu.img_link = (
                    STATIC_URL +
                    "assets/img/bannerpalette/red.png"
                )

        # General parameter
        if request.POST.get('title') != actu.title:
            actu.title = request.POST.get('title')

        if request.POST.get('article') != actu.article:
            actu.article = request.POST.get('article')

        if request.POST.get('short_desc') != actu.short_desc:
            actu.short_desc = request.POST.get('short_desc')

        if request.POST.get('start'):
            if request.POST.get('start') != actu.date:
                actu.date = request.POST.get('start')

        if request.POST.get('end'):
            if request.POST.get('end') != actu.stop_date:
                actu.stop_date = request.POST.get('end')

        # To display this
        if (request.POST.get('is_state') == "on" and
                actu.state == 0):
            actu.state = 1
        if (request.POST.get('is_state') != "on" and
                actu.state == 1):
            actu.state = 0

        # Image format
        if (request.POST.get('format') == "on" and
                actu.format == 0):
            actu.format = 1
        if (request.POST.get('format') != "on" and
                actu.format == 1):
            actu.format = 0

        # Link button
        if actu.external_link == request.POST.get('ext_link'):
            pass
        elif (actu.external_link != (0 or "0") and
                request.POST.get('ext_link') == (0 or "0")):
            actu.external_link = '0'

        elif request.POST.get('ext_link') != ("0" or 0):
            actu.external_link = request.POST.get('ext_link')

        actu.save()
        # Response
        data['error'] = False
        data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
