"""
MANAGE | Office member
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from association.models import MemberOffice


@login_required
def add_office(request):
    data = {}
    data['view'] = 'ajouter-un-membre-du-bureau'
    if (request.POST.get('name') and
            request.POST.get('link') and
            request.POST.get('img_link') and
            request.POST.get('genre')) != "":

        try:
            MemberOffice.objects.create(
                name=request.POST.get('name'),
                role=request.POST.get('role'),
                link=request.POST.get('link'),
                img_link=request.POST.get('img_link'),
                promotion=request.POST.get('promotion'),
                genre=request.POST.get('genre'),
            )

            data['error'] = False
            data['text'] = 'Le membre à été ajouté'

        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout du membre'
    else:
        data['error'] = True
        data['text'] = 'Echec de l\'ajout du membre'

    return data


@login_required
def mod_office(request):
    data = {}
    data['view'] = 'modifier-un-membre-du-bureau'
    try:
        member = MemberOffice.objects.get(id=f"{request.GET.get('id')}")    # noqa
    except ObjectDoesNotExist:
        member = None

    if member:
        if request.POST.get('name') != member.name:
            member.name = request.POST.get('name')

        if request.POST.get('role') != member.role:
            member.role = request.POST.get('role')

        if request.POST.get('link') != member.link:
            member.link = request.POST.get('link')

        if request.POST.get('img_link') != member.img_link:
            member.img_link = request.POST.get('img_link')

        if request.POST.get('promotion') != member.promotion:
            member.promotion = request.POST.get('promotion')

        if request.POST.get('genre') != member.genre:
            member.genre = request.POST.get('genre')

        member.save()
        # Response
        data['error'] = False
        data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
