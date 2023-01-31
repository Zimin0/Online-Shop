from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('dictionary/', include('addwords.urls')),
    path('admin/', admin.site.urls),
    #####################_for_auth_#######################
    path('accounts/', include('django.contrib.auth.urls')) ,
    ######################################################
    path('home/', include('users.urls')),
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

