""" ADD PHOTO METHOD """
from frontpage.forms import ImageForm
from django.contrib.auth.decorators import login_required


@login_required
def add_photo(request):

    form = ImageForm(request.POST, request.FILES)
    data = {}
    data['error'] = 1
    data['text'] = "Formulaire invalide"

    if form.is_valid():
        try:
            form.save()
            data['text'] = "Fichier ajouté"
            data['error'] = 0
        except:    # noqa
            data['error'] = 1
            data['text'] = "Erreur lors de l'ajout du fichier"

    return data
