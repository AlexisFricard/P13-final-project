from django.shortcuts import render

from testimony.models import Testimony

from mastercontrat.settings import MEDIA_URL


def after(request):
    testimony_obj = Testimony.objects.all().filter(state=1)
    testimony_list = []
    testimony_type = []
    for testimony in testimony_obj:
        testi_text = testimony.text.replace('#', "  ")
        job_text = testimony.job.replace('#', "  ")
        testimony_list.append({
            "text": testi_text,
            "author": testimony.author,
            "promotion": testimony.promotion,
            "job": job_text,
            "sector": testimony.sector,
        })
        if testimony.sector not in testimony_type:
            testimony_type.append(testimony.sector)

    data = {
        "media_location": MEDIA_URL,
        "testimony": testimony_list,
        "testimony_type": testimony_type
    }

    return render(request, 'after.html', data)
