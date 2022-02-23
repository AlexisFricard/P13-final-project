"""
Manage Testimony
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from testimony.models import Testimony


@login_required
def add_testimony(request):
    data = {}
    data['view'] = 'ajouter-un-témoignage'
    if (request.POST.get('text') and
            request.POST.get('sector') and
            request.POST.get('author')) != "":
        try:
            Testimony.objects.create(
                text=request.POST.get('text'),
                author=request.POST.get('author'),
                sector=request.POST.get('sector'),
                promotion=request.POST.get('promotion'),
                job=request.POST.get('job'),
            )
            data['error'] = False
            data['text'] = 'Le témoignage à été ajouté'

        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout du témoignage'
    else:
        data['error'] = True
        data['text'] = 'Echec de l\'ajout du témoignage'
    return data


@login_required
def mod_testimony(request):
    data = {}
    data['view'] = 'modifier-un-témoignage'
    try:
        testi = Testimony.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        testi = None

    if testi:
        if request.POST.get('text') != testi.text:
            testi.text = request.POST.get('text')

        if request.POST.get('author') != testi.author:
            testi.author = request.POST.get('author')

        if request.POST.get('promotion') != testi.promotion:
            testi.promotion = request.POST.get('promotion')

        if request.POST.get('job') != testi.job:
            testi.job = request.POST.get('job')

        if request.POST.get('sector') != testi.sector:
            testi.sector = request.POST.get('sector')

        # To display this
        if request.POST.get('is_state') == "on" and testi.state == 0:
            testi.state = 1

        if request.POST.get('is_state') != "on" and testi.state == 1:
            testi.state = 0

        testi.save()
        # Response
        data['error'] = False
        data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
