""" MANAGE FAQs """
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from collabspace.models import Faq


@login_required
def add_faq(request):
    data = {}
    data['view'] = 'ajouter-à-la-faq'

    # Confirm no empty value
    if (request.POST.get('question') and
            request.POST.get('text')) != "":
        try:
            Faq.objects.create(
                question=request.POST.get('question'),
                response=request.POST.get('text')
            )
            data['error'] = False
            data['text'] = 'La faq à été ajoutée'

        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout à la FAQs'
    else:
        data['error'] = True
        data['text'] = 'Echec de l\'ajout à la FAQs'

    return data


@login_required
def mod_faq(request):
    data = {}
    data['view'] = 'modifier-la-faq'
    try:
        faq = Faq.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        faq = None
        # Response
        data['error'] = True
        data['text'] = 'FAQ non trouvable'

    if faq:
        if request.POST.get('delete_it') == "on":
            faq.delete()
            # Response
            data['error'] = False
            data['text'] = 'Suppression terminé'

        else:
            if request.POST.get('question') != faq.question:
                faq.question = request.POST.get('question')

            if request.POST.get('response') != faq.response:
                faq.response = request.POST.get('response')

            if (request.POST.get('is_state') == "on" and
                    faq.state == 0):
                faq.state = 1
            if (request.POST.get('is_state') != "on" and
                    faq.state == 1):
                faq.state = 0

            faq.save()
            # Response
            data['error'] = False
            data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
