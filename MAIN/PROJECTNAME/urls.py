
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from  APPNAME.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("APPNAME.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)