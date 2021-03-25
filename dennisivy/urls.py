
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),



    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name="email_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"), name="password_reset_complete"),

    path('404', include('base.urls')),

]

handler404 = 'base.views.handler404'

handler500 = 'base.views.handler500'

handler400 = 'base.views.handler404'

handler403 = 'base.views.handler404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
