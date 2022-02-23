from django.shortcuts import render

from presentation.models import Team


def presentation_page(request):

    # Set variable
    team = Team.objects.all()
    director_list = []
    staff_list_ = []

    for memb in team:
        if memb.grade == "director":
            director_list.append(memb)
        else:
            staff_list_.append(memb)

    # Set response
    response = {
        "directors": director_list,
        "team": staff_list_,
    }

    return render(request, 'presentation.html', response)
