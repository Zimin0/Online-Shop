from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('addwords.urls')),
    path('admin/', admin.site.urls),
    #####################_for_auth_#######################
    path('accounts/', include('django.contrib.auth.urls')) ,
    ######################################################
    path('home/', include('users.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('myapi.urls')),
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

