"""
mastercontrat URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)


urlpatterns = [

    path('admin/', admin.site.urls),

    # Index + Actualities
    path('', include('frontpage.urls')),
    # Presentation - Team
    path('', include('presentation.urls')),
    # Page 3
    path('', include('testimony.urls')),
    # Page 5
    path('', include('association.urls')),
    # Page 6
    path('', include('ourstudent.urls')),
    # To send mail
    path('', include('contact.urls')),
    # Dashboard
    path('', include('dashboard.urls')),
    # Collaborative Space
    path('', include('collabspace.urls')),
    # Chat application
    path('', include('chat.urls')),

    # Password reset
    path('password-reset/',
        auth_views.PasswordResetView.as_view(       # noqa
            template_name='password_reset/password_reset_form.html'
        ),
        name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Errors
handler404 = 'frontpage.views.error_404'  # noqa
handler400 = 'frontpage.views.error_400'  # noqa
handler403 = 'frontpage.views.error_403'  # noqa
handler500 = 'frontpage.views.error_500'  # noqa