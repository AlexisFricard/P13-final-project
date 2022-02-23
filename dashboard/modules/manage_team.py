"""
MAIN FILE
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from presentation.models import Team


@login_required
def add_team(request):
    data = {}
    data['view'] = 'ajouter-un-membre-de-l-équipe-pédagogique'
    # Confirm no empty value
    if (request.POST.get('name') and
            request.POST.get('link') and
            request.POST.get('img_link') and
            request.POST.get('status1')) != "":

        try:
            Team.objects.create(
                name=request.POST.get('name'),
                link=request.POST.get('link'),
                img_link=request.POST.get('img_link'),
                status1=request.POST.get('status1'),
                status2=request.POST.get('status2'),
                status3=request.POST.get('status3'),
                status4=request.POST.get('status4'),
                status5=request.POST.get('status5'),
                grade=request.POST.get('grade'),
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
def mod_team(request):
    data = {}
    data['view'] = 'modifier-un-membre-de-l-équipe-pédagogique'
    try:
        member = Team.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        member = None

    if member:
        if request.POST.get('name') != member.name:
            member.name = request.POST.get('name')

        if request.POST.get('grade') != member.grade:
            member.grade = request.POST.get('grade')

        if request.POST.get('link') != member.link:
            member.link = request.POST.get('link')

        if request.POST.get('img_link') != member.img_link:
            member.img_link = request.POST.get('img_link')

        if request.POST.get('status1') != member.status1:
            member.status1 = request.POST.get('status1')
        if request.POST.get('status2') != member.status2:
            member.status2 = request.POST.get('status2')
        if request.POST.get('status3') != member.status3:
            member.status3 = request.POST.get('status3')
        if request.POST.get('status4') != member.status4:
            member.status4 = request.POST.get('status4')
        if request.POST.get('status5') != member.status5:
            member.status5 = request.POST.get('status5')

        member.save()

        # Response
        data['error'] = False
        data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
