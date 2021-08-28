from django.contrib import admin
from .models import (
    Actuality, Faq, Link, Promotion, Testimony,
    Ticket, AuthorMessageTicket)
# Register your models here.

admin.site.register(Actuality)
admin.site.register(Faq)
admin.site.register(Link)
admin.site.register(Promotion)
admin.site.register(Testimony)
admin.site.register(Ticket)
admin.site.register(AuthorMessageTicket)
