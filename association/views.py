from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import logging

# TODO Import date time
# from datetime import datetime

from association.models import MemberOffice
from mastercontrat.settings import MEDIA_URL


def association(request):
    print(MEDIA_URL)

    # === For automatic selection ===
    # now = datetime.now()
    # year = str(now.year) + " - " + str(now.year + 1)

    data = {}

    try:
        president = MemberOffice.objects.get(role="president")
        vice = MemberOffice.objects.get(role="vice")
        secretary = MemberOffice.objects.get(role="secretary")
        treasurer = MemberOffice.objects.get(role="treasurer")

        data = {
            "president": president,
            "vice": vice,
            "secretary": secretary,
            "treasurer": treasurer,
        }

    except ObjectDoesNotExist as error:
        logging.info('==== There is an error ====')
        logging.error(error)
        pass

    data["media_location"] = MEDIA_URL
    return render(request, 'association.html', data)
