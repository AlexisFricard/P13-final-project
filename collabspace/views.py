"""
COLLABSPACE | Main file
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from mastercontrat.settings import MEDIA_URL
from frontpage.forms import ImageForm
from frontpage.models import Image
from modules.add_img import add_photo

from .models import (
    Faq, Link
)


@login_required
def myspace(request, inview):
    if request.method == "POST":
        imgs = Image.objects.filter(title=f'img_{request.user.id}')

        # TODO : delete img from bucket
        for img in imgs:
            img.delete()

        data = add_photo(request)
        return redirect('myaccount')

    if request.method == "GET":
        if inview:
            inview = 'inview_' + inview
        else:
            inview = False

        # GET FAQ
        faq_list = []
        faq_objects = Faq.objects.all().filter(state=1)
        for faq in faq_objects:
            faq_response = faq.response.replace("#", "  ")
            faq_list.append({
                "question": faq.question,
                "response": faq_response,
                "id": faq.id,
            })
        # GET lINK
        link_list = []
        link_objects = Link.objects.all().filter(state=1)
        for linksave in link_objects:
            link_list.append({
                "title": linksave.title,
                "link": linksave.link,
            })

        data = {
            "faq": faq_list,
            "links": link_list,
            "form": ImageForm(),
        }
        if inview:
            return render(request, f'inviews_myspace/{inview}.html', data)
        else:
            return render(request, 'myspace.html', data)


@login_required
def myaccount(request):

    try:
        img = Image.objects.get(title=f'img_{request.user.id}')
        link = img.image
        media = 1
        media_url = MEDIA_URL
    except ObjectDoesNotExist:
        link = None
        media = 0
        media_url = None

    return render(request, "myaccount.html", {
        "img": link,
        'media': media,
        'media_url': media_url,
        })


@login_required
def log_out(request):
    logout(request)
    return redirect("index")


def log_in(request):
    if request.method == "POST":
        # AUTHENTIFICATE FORMS
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # LOG USER
            login(request, form.user_cache)
            return redirect('myspace', 'home')
    return redirect('index')
