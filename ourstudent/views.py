from django.shortcuts import render

import json

from ourstudent.models import Promotion
from mastercontrat.settings import MEDIA_URL


# Create your views here.
def ourstudent(request):

    # Convert string to dict with json
    def conv_str_to_dict(col):

        data_ = json.loads(col.replace("'", "\""))

        return {
            "title": data_['title'],
            "students": data_['students'],
        }

    # To display promotions
    promotion_list = []
    promotions = Promotion.objects.all().order_by('-date')

    for promotion in promotions:

        if promotion.img_link.startswith('https'):
            media = False
        else:
            media = True

        promotion_list.append({
            "media": media,
            "img_link": promotion.img_link,
            "formation": promotion.formation,
            "date": promotion.date,
            "col1": conv_str_to_dict(promotion.col1),
            "col2": conv_str_to_dict(promotion.col2),
            "col3": conv_str_to_dict(promotion.col3),
        })

    return render(request, 'ourstudent.html', {
        "promotions": promotion_list,
        "media_location": MEDIA_URL,
    })
