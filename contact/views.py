from django.shortcuts import render
from django.core.mail import send_mail


# Send email
def contact(request):
    if request.method == "POST":
        send_mail(
            f'{request.POST.get("object")}',
            (
                f'Nom : {request.POST.get("name")}\n' +
                f'Email : {request.POST.get("email")}\n' +
                f'Tél : {request.POST.get("phone_number")}' +
                f'\n\nMessage :\n\n{request.POST.get("message")}'
            ),
            'noreply@masteraffairescontrats-poitiers.fr',
            ['contact@masteraffairescontrats-poitiers.fr'],
            fail_silently=False,
        )
        return render(request, "contact.html", {'email_send': True})
    return render(request, "contact.html")
