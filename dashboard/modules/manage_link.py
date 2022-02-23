"""
COLLABSPACE | MANAGE LINK
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from collabspace.models import Link


@login_required
def add_link(request):
    data = {}
    data['view'] = 'ajouter-un-lien'
    # Confirm no empty value
    if (request.POST.get('title') and
            request.POST.get('link')) != "":
        try:
            Link.objects.create(
                title=request.POST.get('title'),
                link=request.POST.get('link')
            )
            data['error'] = False
            data['text'] = 'Le lien à été ajouté'

        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout du lien'
    else:
        data['error'] = True
        data['text'] = 'Echec de l\'ajout du lien'
    return data


@login_required
def mod_link(request):
    data = {}
    data['view'] = 'modifier-un-lien'

    try:
        link = Link.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        link = None
        # Response
        data['error'] = True
        data['text'] = 'Lien non trouvable'

    if link:
        if request.POST.get('delete_it') == "on":
            link.delete()
            # Response
            data['error'] = False
            data['text'] = 'Suppression terminé'

        else:
            if request.POST.get('title') != link.title:
                link.title = request.POST.get('title')

            if request.POST.get('link') != link.link:
                link.link = request.POST.get('link')

            if (request.POST.get('is_state') == "on" and
                    link.state is not True):
                link.state = True
            if (request.POST.get('is_state') != "on" and
                    link.state is True):
                link.state = False

            link.save()
            data['error'] = False
            data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
