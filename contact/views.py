from django.shortcuts import render
from django.core.mail import send_mail


# Send email
def contact(request):
    if request.method == "POST":
        response = True
        text = 'L\'email n\'as pas été envoyé'
        error = 1
        try:
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

            text = 'L\'email as été envoyé'
            error = 0
        except ConnectionError:
            text = 'L\'email n\'as pas été envoyé'
            error = 1

        return render(request, "contact.html", {
            'response': response,
            'response_text': text,
            'response_error': error,
        })
    return render(request, "contact.html")
