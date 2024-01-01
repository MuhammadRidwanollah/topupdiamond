from django.contrib import admin
from django.urls import path
from web.views import home, menu
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu),
    path('', home),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)