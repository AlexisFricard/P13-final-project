from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import requests
from requests.exceptions import MissingSchema
import secrets
import os

from frontpage.forms import ImageForm
from frontpage.models import (
    Actuality, Faq, Link, Promotion, Testimony,
    Ticket, AuthorMessageTicket
    )

if os.getenv("ENV") == "PRODUCTION":
    from mastercontrat.settings import MEDIA_URL
else:
    from mastercontrat.dev_settings import MEDIA_URL


# Global method
def get_actuality(url, start, end):
    url = MEDIA_URL + url
    img_exist = 0
    same_day = 0

    # media url
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            img_exist = 1
    except MissingSchema:
        img_exist = 0

    # free url
    if not img_exist:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                img_exist = 1
        except MissingSchema:
            img_exist = 0

    # Test dates
    if start == end:
        same_day = 1

    return img_exist, same_day


# Views method
def index(request):

    actualities_obj = Actuality.objects.all()
    actu_list = []
    for actu in actualities_obj:

        # Test img_link url
        img_exist, same_day = get_actuality(
            actu.img_title,
            actu.date,
            actu.stop_date
        )
        actu_list.append({
            "id":       actu.id,
            "title":    actu.title,
            "start":    actu.date,
            "end":      actu.stop_date,
            "article":  actu.article,
            "img_link": actu.img_title,
            "same_day": same_day,
            "img_exist": img_exist,
        })
    actualities = {
        "actualities":      actu_list,
        "media_location":   MEDIA_URL,
    }
    return render(request, 'index.html', actualities)


def presentation(request):
    return render(request, 'presentation.html')


def after(request):
    testimony_obj = Testimony.objects.all()
    testimony_list = []
    for testimony in testimony_obj:
        testimony_list.append({
            "text": testimony.text,
            "author": testimony.author,
            "sector": testimony.sector
        })
    data = {
        "media_location": MEDIA_URL,
        "testimony": testimony_list
    }
    return render(request, 'after.html', data)


def ourstudent(request):

    promotion_obj = Promotion.objects.all()
    promotion_list = []
    for promotion in promotion_obj:
        promotion_list.append({
            "banner": promotion.title,
            "description": promotion.description,
            "img_title": promotion.img_title,
        })
    data = {
        "media_location": MEDIA_URL,
        "promotions": promotion_list
    }
    return render(request, 'ourstudent.html', data)


def association(request):
    return render(request, 'association.html')


def myspace(request):

    if request.method == "POST":
        # AUTHENTIFICATE FORMS
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # LOG USER
            login(request, form.user_cache)
            return redirect('myspace')
        else:
            # AUTHENTIFICATE FORMS
            form = AuthenticationForm(request)
            return render(request, 'myspace.html')

    elif request.method == "GET":
        # REQUEST STAFF
        list_of_staff = User.objects.filter(
            is_staff=True
            ).filter(is_active=True)
        if request.user.is_authenticated:
            # GET FAQ
            faq_list = []
            faq_objects = Faq.objects.all()
            for faq in faq_objects:
                faq_list.append({
                    "question": faq.question,
                    "response": faq.response
                })
            # GET lINK
            link_list = []
            link_objects = Link.objects.all()
            for linksave in link_objects:
                link_list.append({
                    "title": linksave.title,
                    "link": linksave.link
                })

            # GET TICKETS
            ticket_list = []
            ticket_objects = Ticket.objects.filter(
                author=request.user.username
                )
            for ticket in ticket_objects:
                ticket_list.append({
                    "title": ticket.title,
                    "id": ticket.id,
                    "state": ticket.state
                })
            return render(request, 'myspace.html', {
                "staff": len(list_of_staff),
                "faq": faq_list,
                "links": link_list,
                "tickets": ticket_list
            })
        else:
            form = AuthenticationForm(request)
            return render(request, 'myspace.html')


def actuality(request):
    if request.method == "GET":
        actu_id = request.GET.get("actuId")
        data = {}
        try:
            actu = Actuality.objects.get(id=actu_id)
            img_exist, same_day = get_actuality(
                actu.img_title,
                actu.date,
                actu.stop_date
                )

            data = {
                "id":               actu.id,
                "title":            actu.title,
                "start":            actu.date,
                "end":              actu.stop_date,
                "article":          actu.article,
                "img_link":         actu.img_title,
                "same_day":         same_day,
                "img_exist":        img_exist,
                "media_location":   MEDIA_URL
            }
            return render(request, "actuality.html", data)

        except ObjectDoesNotExist:
            return redirect("index")


@login_required
def helpdashboard(request):

    if request.user.is_staff:
        messages_object = AuthorMessageTicket.objects.all().order_by('date')
        ticket_object = Ticket.objects.all()
        list_of_tickets = []
        for ticket in ticket_object:
            messages_object = AuthorMessageTicket.objects.filter(
                ticket_id=ticket.id
                ).order_by('date')
            list_of_tickets.append({
                "title": ticket.title,
                "date": messages_object[0].date.strftime("%d/%m/%Y, %H:%M"),
                "state": ticket.state,
                "id": ticket.id
            })
        data = {
            "tickets": list_of_tickets
        }
        return render(request, 'helperdashboard.html', data)
    else:
        return redirect('myspace')


@login_required
def manage(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
        return render(request, "manage.html", {
            "form": ImageForm()
            })
    else:
        return redirect("myspace")


@login_required
def ticket(request):

    if request.method == "GET":
        t_id = request.GET.get("id")
        messages_object = AuthorMessageTicket.objects.filter(
            ticket_id=t_id
            ).order_by('date')
        if messages_object:
            if (messages_object[0].author == request.user.username or
                    request.user.is_staff):    # noqa

                list_of_messages = []
                for msg in messages_object:
                    list_of_messages.append({
                        "author":   msg.author,
                        "msg":      msg.message,
                        "date":     msg.date
                    })

                data = {
                    "messages": list_of_messages
                }

                return render(request, "ticket.html", data)
            else:
                return redirect("myspace")
        else:
            return redirect("myspace")


@login_required
def myaccount(request):
    # GET TICKETS
    ticket_list = []
    ticket_objects = Ticket.objects.filter(author=request.user.username)
    for ticket in ticket_objects:
        ticket_list.append({
            "title": ticket.title,
            "id": ticket.id,
            "state": ticket.state
        })
    return render(request, "myaccount.html", {"tickets": ticket_list})


@login_required
def log_out(request):

    logout(request)
    return redirect("index")


@csrf_exempt
def add_user(request):
    if request.user.is_superuser:
        if request.method == "POST":
            # Confirm no empty value
            if (request.POST.get('firstname') and
                    request.POST.get('lastname') and
                    request.POST.get('email')) != "":
                # Confirm email
                if request.POST.get('email') == request.POST.get('emailconfirm'):
                    # generate password
                    password = secrets.token_urlsafe()
                    password = password[0:10]
                    # Is a staff
                    if request.POST.get('staff') == "true":
                        staff = 1
                    else:
                        staff = 0
                    # Try to create user
                    username = (
                        request.POST.get('firstname') +
                        request.POST.get('lastname')
                    )
                    try:
                        User.objects.create_user(
                            username=username,
                            email=request.POST.get('email'),
                            is_staff=staff,
                            password=password,
                        )
                        return JsonResponse({
                            "resp": True,
                            "password": password,
                            "id": username,
                            "email": request.POST.get('email')
                            })
                    # User allready exist
                    except:    # noqa
                        return JsonResponse({
                            "resp": False,
                            "state": "L'utilisateur existe déjà"
                            })
                # Confirmation email fail
                else:
                    return JsonResponse({
                        "resp": False,
                        "state": "La confirmation d'email a échoué"
                        })
            # One field is empty
            else:
                return JsonResponse({
                    "resp": False,
                    "state": "Un champ n'as pas été rempli"
                    })


@csrf_exempt
def add_data(request):
    if request.method == "POST":
        # ACTUALITY
        if request.POST.get("box") == "actuality":
            if (request.POST.get('title') and
                    request.POST.get('article')) != "":
                if "#" in request.POST.get('article'):
                    d_artic = request.POST.get('article')
                    d_artic = d_artic.replace("#", "  ")
                else:
                    d_artic = request.POST.get('article')
                try:
                    Actuality.objects.create(
                        title=request.POST.get('title'),
                        date=request.POST.get('start'),
                        stop_date=request.POST.get('end'),
                        article=d_artic,
                        img_title=request.POST.get('link'),
                    )
                    return JsonResponse({"state": True})
                except:    # noqa
                    return JsonResponse({"state": False})
            else:
                return JsonResponse({
                    "resp": False,
                    "state": "Un champ n'as pas été rempli"
                    })

        # FAQ
        elif request.POST.get('box') == "faq":
            # Confirm no empty value
            if (request.POST.get('question') and
                    request.POST.get('text')) != "":
                try:
                    Faq.objects.create(
                        question=request.POST.get('question'),
                        response=request.POST.get('text')
                    )
                    return JsonResponse({"resp": True})
                # Allready exist
                except:    # noqa
                    return JsonResponse({"resp": False})
            # Empty field
            else:
                return JsonResponse({"resp": False})

        # LINK
        elif request.POST.get('box') == "link":
            # Confirm no empty value
            if (request.POST.get('title') and
                    request.POST.get('link')) != "":
                try:
                    Link.objects.create(
                        title=request.POST.get('title'),
                        link=request.POST.get('link')
                    )
                    return JsonResponse({"resp": True})
                # Allready exist
                except:    # noqa
                    return JsonResponse({"resp": False})
            # Empty field
            else:
                return JsonResponse({"resp": False})

        # TESTIMONY
        elif request.POST.get('box') == "testimony":
            # Confirm no empty value
            if (request.POST.get('text') and
                    request.POST.get('sector') and
                    request.POST.get('author')) != "":
                try:
                    Testimony.objects.create(
                        text=request.POST.get('text'),
                        author=request.POST.get('author'),
                        sector=request.POST.get('sector')
                    )
                    return JsonResponse({"resp": True})
                # Allready exist
                except:    # noqa
                    return JsonResponse({"resp": False})
            # Empty field
            else:
                return JsonResponse({"resp": False})

        # PROMOTION
        elif request.POST.get('box') == "promotion":
            # Confirm no empty value
            if (request.POST.get('title') and
                    request.POST.get('description') and
                    request.POST.get('img_title')) != "":
                try:
                    Promotion.objects.create(
                        title=request.POST.get('title'),
                        description=request.POST.get('description'),
                        img_title=request.POST.get('img_title')
                    )
                    return JsonResponse({"resp": True})
                # Allready exist
                except:    # noqa
                    return JsonResponse({"resp": False})
            # Empty field
            else:
                return JsonResponse({"resp": False})

        # TICKET
        if request.POST.get("box") == "ticket":
            if (request.POST.get('title') and
                    request.POST.get('text')) != "":
                # try to get ticket allready registred
                try:
                    ticket = Ticket.objects.get(
                        title=request.POST.get('title'),
                        author=request.user.username
                        )
                    return JsonResponse({
                        "state": False,
                        "id": ticket.id
                        })
                # if not exist
                except ObjectDoesNotExist:    # noqa
                    doesnt_exist = True

                if doesnt_exist:
                    Ticket.objects.create(
                        title=request.POST.get('title'),
                        author=request.user.username
                    )

                    ticket = Ticket.objects.get(
                        title=request.POST.get('title')
                        )

                    AuthorMessageTicket.objects.create(
                        ticket_id=ticket.id,
                        author=request.user.username,
                        message=request.POST.get('text')
                    )
                    return JsonResponse({"id": ticket.id})

                return JsonResponse({"state": False})
            else:
                return JsonResponse({"resp": False})


def error_400(request, exception, **kwargs):
    return render(request, 'error/400.html')


def error_403(request, exception, **kwargs):
    return render(request, 'error/403.html')


def error_404(request, exception):
    return render(request, 'error/404.html')


def error_500(request, *args, **kwargs):
    return render(request, 'error/500.html')
