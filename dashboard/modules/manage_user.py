"""
MANAGE | Users
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import secrets


def add_user(request):
    data = {}
    data['view'] = 'ajouter-un-utilisateur'
    # Confirm no empty value
    if (request.POST.get('firstname') and
            request.POST.get('lastname') and
            request.POST.get('email')) != ("" or None):
        # Confirm email
        if (request.POST.get('email') ==
                request.POST.get('emailconfirm')):
            # generate password
            password = secrets.token_urlsafe()
            password = password[0:10]

            # Try to create user
            username_ = (
                request.POST.get('firstname') +
                request.POST.get('lastname')
            ).lower()

            User.objects.create_user(
                first_name=request.POST.get('firstname'),
                last_name=request.POST.get('lastname'),
                username=username_,
                email=request.POST.get('email'),
                password=password,
                )

            if request.POST.get('is_staff') == "on":
                user = User.objects.get(username=username_)
                user.is_staff = True
                user.is_superuser = True
                user.save()

            data['error'] = False
            data['text'] = 'Utilisateur ajouté'

            try:
                send_mail(
                    'Bienvenue sur le site de l\'association des Masters Contrats de Poitiers',   # noqa                          (
                    (
                        f'Bienvenue {request.POST.get("firstname")} !\n\n' +    # noqa
                        f'Vous vous êtes fait inscrire par {request.user} ' +   # noqa
                        'sur le site de l\'association des Masters Contrats de Poitiers.\n' +   # noqa
                        'Voici donc votre identifiant ainsi que votre mot de passe :\n\n' +   # noqa
                        f'Identifiant : {username_}\nMot de passe : {password}\n\n' +   # noqa
                        'Bien à vous,\nLe bureau !\n\n'
                    ),
                    'noreply@masteraffairescontrats-poitiers.fr',
                    [f'{request.POST.get("email")}'],
                    fail_silently=False,
                )
                data['text'] += '\nL\'email à été envoyé'

            except ConnectionRefusedError:
                data['error'] = True
                data['text'] += '\nEchec de l\'envoie du mail'
        else:
            # EMAIL NOT CONFIRMED
            data['error'] = True
            data['text'] = 'Echec de l\'ajout de l\'utilisateur'
    else:
        # BAD ID
        data['error'] = True
        data['text'] = 'Echec de l\'ajout de l\'utilisateur'

    return data


@login_required
def mod_user(request):
    data = {}
    data['view'] = 'modifier-un-utilisateur'

    try:
        user = User.objects.get(id=f"{request.GET.get('id')}")
    except ObjectDoesNotExist:
        user = None
        data['error'] = True
        data['text'] = 'L\'utilisateur est introuvable'

    if user:
        if request.POST.get('email') != (user.email and ""):
            user.email = request.POST.get('email')

        if request.POST.get('username') != (user.username and ""):
            user.username = request.POST.get('username')

        if not request.POST.get('name_'):
            if (request.POST.get('is_staff') == "on" and
                    user.is_staff is not True):
                user.is_staff = True
                user.is_superuser = True

            elif (request.POST.get('is_staff') is None and
                    user.is_staff is True):
                user.is_staff = False
                user.is_superuser = False

            user.save()
            # Response
            data['error'] = False
            data['text'] = 'Élément modifié'
            try:
                send_mail(
                    (
                        'Changements sur le site de l\'association ' +    # noqa
                        'des Masters Contrats de Poitiers'
                    ),
                    (
                        f'{user.first_name},\n\n' +
                        f'{request.user} a changé votre pseudo de connection' +    # noqa
                        ' pour le site de l\'association.\n' +
                        'Voici votre nouvel identifiant :\n\n' +
                        f'Identifiant : {user.username}\n\n' +
                        'Bien à vous,\nLe bureau !\n\n'
                    ),
                    '',
                    [f'{request.POST.get("email")}'],
                    fail_silently=False,
                )
                data['text'] += '\nEmail envoyé'

            except ConnectionRefusedError:
                data['error'] = True
                data['text'] += '\nEchec de l\'envoie du mail'
        else:
            data['error'] = False

    return data
