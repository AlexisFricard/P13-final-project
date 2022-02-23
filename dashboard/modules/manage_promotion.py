"""
Manage promotion
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from ourstudent.models import Promotion


@login_required
def add_promotion(request):
    data = {}
    data['view'] = 'ajouter-une-promotion'
    if (request.POST.get('img_link') and
            request.POST.get('formation') and
            request.POST.get('date')) != (None or ""):

        _img_link = request.POST.get('img_link')
        _formation = request.POST.get('formation')
        _date = request.POST.get('date')

        col1_name = request.POST.get('col1-title')
        col2_name = request.POST.get('col2-title')
        col3_name = request.POST.get('col3-title')

        def get_list_of_students(col):
            list_of_students = []
            for y in range(1, 13):
                try:
                    student = request.POST.get(f'col{col}-student{y}-name')
                    if not student:
                        student = ''
                    if len(student) >= 2:   # noqa
                        list_of_students.append({
                            "name": request.POST.get(f'col{col}-student{y}-name'),   # noqa
                            "link": {
                                "target": request.POST.get(f'col{col}-student{y}-target'),   # noqa
                                "url": request.POST.get(f'col{col}-student{y}-link')   # noqa
                            }
                        })

                except ValueError or TypeError:
                    pass
                return list_of_students

        _col1 = {
            "title": col1_name,
            "students": get_list_of_students(1),
        }
        _col2 = {
            "title": col2_name,
            "students": get_list_of_students(2),
        }
        _col3 = {
            "title": col3_name,
            "students": get_list_of_students(3),
        }

        try:
            Promotion.objects.create(
                img_link=_img_link,
                formation=_formation,
                date=_date,
                col1=_col1,
                col2=_col2,
                col3=_col3
            )
            data['error'] = False
            data['text'] = 'La promotion à été ajoutée'
        except:    # noqa
            data['error'] = True
            data['text'] = 'Echec de l\'ajout de la promotion'
    else:
        data['error'] = True
        data['text'] = 'Echec de l\'ajout de la promotion'

    return data


@login_required
def mod_promotion(request):
    data = {}
    data['view'] = 'modifier-une-promotion'
    try:
        promo = Promotion.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        promo = None

    if promo:
        if request.POST.get('img_link') != promo.img_link:
            promo.img_link = request.POST.get('img_link')
        if request.POST.get('formation') != promo.formation:
            promo.formation = request.POST.get('formation')
        if request.POST.get('date') != promo.date:
            promo.date = request.POST.get('date')

        # TODO: 3 column to change
        promo.save()
        # Response
        data['error'] = False
        data['text'] = 'Élément modifié'
    else:
        data['error'] = True
        data['text'] = 'Echec de la modification'

    return data
