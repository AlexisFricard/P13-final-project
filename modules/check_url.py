
import requests
# from requests.exceptions import (
#     MissingSchema, InvalidSchema, InvalidURL,
#     ConnectionError
# )

from mastercontrat.settings import MEDIA_URL


# Test url of img link
def check_url(url):

    # Set variables
    url_bucket = MEDIA_URL + url
    img_exist = 0

    # Step 1 - media url
    try:
        resp_bucket = requests.get(url_bucket)
        if resp_bucket.status_code == 200:
            img_exist = 1
    except:    # noqa
        img_exist = 0

    # Step 2 - free url
    if not img_exist:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                img_exist = 1
        except:    # noqa
            img_exist = 0

    return img_exist
