"""
Dashboard | Main file
"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from frontpage.forms import ImageForm
from frontpage.models import (
    Actuality, Image
)
from collabspace.models import (
    Link, Faq
)
from modules.add_img import add_photo

from testimony.models import Testimony
from ourstudent.models import Promotion
from association.models import MemberOffice
from presentation.models import Team

from mastercontrat.settings import MEDIA_URL

from .modules import (
    manage_actuality, manage_faq, manage_link,
    manage_office, manage_team, manage_testimony,
    manage_promotion, manage_user
)


# ======Response======= #
def response_state(state):
    global responseState
    responseState = state


def response_text(text):
    global responseText
    responseText = text


def response_error(bool_):
    global responseError
    responseError = bool_


response_state(False)
response_text('')
response_error(0)
# ====================== #


@login_required
def dashboard(request, inview):
    if request.user.is_staff:
        data = 0

        if inview:
            inview = 'inview-' + inview
        else:
            inview = False

        # PHOTO
        if request.method == "POST":
            response_state(True)
            data = add_photo(request)
            response_text(data['text'])
            response_error(data['error'])

        users_obj = User.objects.all().order_by('id')
        faq_obj = Faq.objects.all().order_by('id')
        links = Link.objects.all().order_by('id')
        imgs = Image.objects.all().order_by('title')
        actualities = Actuality.objects.all().order_by('-date')
        testimonies = Testimony.objects.all().order_by('id')
        member_offices = MemberOffice.objects.all()
        team = Team.objects.all().order_by('name')
        # TODO display promotions
        promotions = Promotion.objects.all().order_by('-date')

        director_list = []
        staff_list_ = []

        for memb in team:
            if memb.grade == "director":
                director_list.append(memb)
            else:
                staff_list_.append(memb)

        data = {
            "media_url": MEDIA_URL,
            "users": users_obj,
            "faqs": faq_obj,
            "links": links,
            "data": data,
            "form": ImageForm(),
            "imgs": imgs,
            "actus": actualities,
            "testis": testimonies,
            "member_office": member_offices,
            "directors": director_list,
            "team": staff_list_,
            "promotions": promotions,
            "response": responseState,
            "response_text": responseText,
            "response_error": responseError
            }
        response_state(False)
        response_error(0)
        response_text('')

        if inview:
            return render(request, f"inviews_dashboard/{inview}.html", data)
        else:
            return render(request, "inviews_dashboard/inview-home.html", data)


@login_required
def add_data(request):
    if request.user.is_superuser:
        response_state(True)
        if request.method == "POST":
            box = request.POST.get("box")
            data = {}
            data['error'] = True
            data['text'] = 'No box matching'
            data['view'] = 'home'
            # ACTUALITY
            if box == "actuality":
                data = manage_actuality.add_actu(request)

            # FAQ
            elif box == "faq":
                data = manage_faq.add_faq(request)

            # LINK
            elif box == "link":
                data = manage_link.add_link(request)

            # TESTIMONY
            elif box == "testimony":
                data = manage_testimony.add_testimony(request)

            # PROMOTION TODO
            elif box == "promotion":
                data = manage_promotion.add_promotion(request)

            # MEMBERS
            elif box == "member":
                if request.POST.get('box-2') == "team":
                    data = manage_team.add_team(request)

                elif request.POST.get('box-2') == "office":
                    data = manage_office.add_office(request)

            # USERS
            elif box == "user":
                data = manage_user.add_user(request)

            if data['error']:
                response_error(1)

            response_text(data['text'])

            return redirect('dashboard', data['view'])
    else:
        return redirect('myspace')


@login_required
def mod_data(request):
    if request.user.is_superuser or (
            request.user.username == request.POST.get('name_')):
        response_state(True)
        if request.method == "POST":

            box = request.GET.get('dbdata')
            data = {}
            data['error'] = True
            data['text'] = 'No box matching'
            data['view'] = 'home'
            # ACTUALITY
            if box == "actuality":
                data = manage_actuality.mod_actu(request)

            # FAQ
            elif box == "faq":
                data = manage_faq.mod_faq(request)

            # LINK
            elif box == "link":
                data = manage_link.mod_link(request)

            # TESTIMONY
            elif box == "testimony":
                data = manage_testimony.mod_testimony(request)

            # PROMOTION TODO
            elif box == "promotion":
                data = manage_promotion.mod_promotion(request)

            # MEMBERS
            elif box == "team":
                data = manage_team.mod_team(request)

            elif box == "office":
                data = manage_office.mod_office(request)

            if box == "user":
                data = manage_user.mod_user(request)

            if data['error']:
                response_error(1)
            else:
                response_error(0)

            response_text(data['text'])

        if not request.POST.get('name_'):
            return redirect('dashboard', data['view'])
        else:
            return redirect('myaccount')
    else:
        return redirect('myspace')


@login_required
def delete_it(request):
    if request.user.is_superuser or (
            request.user.username == request.POST.get('name_')):
        id_ = request.GET.get('id')
        type_ = request.GET.get('t')
        username_ = request.GET.get('username')
        view = 'home'
        response_state(True)

        if type_ == "img":
            img_ = Image.objects.get(id=id_)
            img_.delete()
            view = 'toutes-les-photos'
            response_text('Photo supprimée')

        if type_ == "actu":
            actu_ = Actuality.objects.get(id=id_)
            actu_.delete()
            view = 'modifier-une-actualité'
            response_text('Actualité supprimée')

        if type_ == "testi":
            testi_ = Testimony.objects.get(id=id_)
            testi_.delete()
            view = 'modifier-un-témoignage'
            response_text('Témoignage supprimé')

        if type_ == "office":
            member_ = MemberOffice.objects.get(id=id_)
            member_.delete()
            view = 'modifier-un-membre-du-bureau'
            response_text('Membre du bureau supprimé')

        if type_ == "team":
            member_ = Team.objects.get(id=id_)
            member_.delete()
            view = 'modifier-un-membre-de-l-équipe-pédagogique'
            response_text('Membre de l\'équipe pédagogique supprimé')

        if type_ == "user":
            if request.user.is_staff or (
                    username_ == request.user.username):
                user = User.objects.get(id=id_)
                user.delete()
                view = 'modifier-un-utilisateur'
                response_text('Utilisateur supprimé')

        if username_:
            return redirect("index")
        else:
            return redirect("dashboard", view)
    else:
        return redirect('myspace')
