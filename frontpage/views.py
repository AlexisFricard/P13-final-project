"""
FRONTPAGE | Main file
"""
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import datetime

from frontpage.models import Actuality
from modules.check_url import check_url

from mastercontrat.settings import MEDIA_URL


# ------------- #
# Global method #
# ------------- #
def convert_to_markdown(string):
    if "#" in string:
        md_string = string.replace("#", "  ")
    else:
        md_string = string
    return md_string


def get_actuality(url, start, end):

    same_day = 0
    if url.startswith('https'):
        img_exist = check_url(url)
    else:
        img_exist = 1

    # Step 3- Test dates
    if start == end:
        same_day = 1

    # Return datas
    return img_exist, same_day


def wrap_actu(actu):

    # Get actuality function
    # To test URL and day
    img_exist, same_day = get_actuality(
        actu.img_title,
        actu.date,
        actu.stop_date
    )

    # Convert to markdown
    d_artic = convert_to_markdown(actu.article)
    d_short = convert_to_markdown(actu.short_desc)

    if actu.img_title.startswith('https'):
        media = None
    else:
        media = True

    # Append actu details
    resp = {
            "id":       actu.id,
            "title":    actu.title,
            "start":    actu.date,
            "end":      actu.stop_date,
            "img_format": actu.format,
            "article":  d_artic,
            "short_desc": d_short,
            "img_link": actu.img_title,
            "same_day": same_day,
            "img_exist": img_exist,
            "ext_link": actu.external_link,
            "media": media,
            "media_location": MEDIA_URL,
        }

    return resp


# Set cookie
def setcookie(request):
    response = HttpResponse("index")
    response.set_cookie('cookie_accord', 'accepted')
    return response


# ------------- #
# Views method  #
# ------------- #
def index(request):

    # Cookie
    value = request.COOKIES.get('cookie_accord')
    if value is None:
        cookie_accepted = False
    else:
        cookie_accepted = True

    # Actualities
    actualities_obj = Actuality.objects.all().order_by('-date').filter(state=1)
    actu_list = []
    actu_list_debug = []
    actualities_nb = False

    for actu in actualities_obj:

        today = datetime.date.today()

        if (today < actu.date or
                today == actu.date or
                len(actualities_obj) <= 3):

            actu_list.append(wrap_actu(actu))

        actu_list_debug.append(wrap_actu(actu))

    # If more than 2 actuality
    # Else, return list or no one
    if len(actu_list) > 3:
        # Keep only 3 last
        actu_list = actu_list[-3:]
        # To unset fixed actu
        actualities_nb = True
    else:
        # To keep fixed actu
        actu_list = actu_list_debug[-3:]
        actualities_nb = False

    # Set data dict
    data = {
        "actualities":      actu_list,
        "media_location":   MEDIA_URL,
        "cookie":           cookie_accepted,
        "actualities_nb":   actualities_nb,
    }

    # Return index
    return render(request, 'index.html', data)


def actualities(request):
    list_actu = []
    actu = Actuality.objects.all().order_by("-date").filter(state=1)

    for actuality in actu:

        list_actu.append(wrap_actu(actuality))

    return render(request, "actualities.html", {
            "data":             list_actu,
            "media_location":   MEDIA_URL,
        }
    )


def actuality(request):
    if request.method == "GET":
        actu_id = request.GET.get("id")
        data = {}
        try:
            actu = Actuality.objects.get(id=actu_id)
            data = wrap_actu(actu)

            return render(request, "actuality.html", data)

        except ObjectDoesNotExist:
            return redirect("index")


def error_400(request, exception, **kwargs):
    return render(request, 'error/400.html')


def error_403(request, exception, **kwargs):
    return render(request, 'error/403.html')


def error_404(request, exception):
    return render(request, 'error/404.html')


def error_500(request, *args, **kwargs):
    return render(request, 'error/500.html')
