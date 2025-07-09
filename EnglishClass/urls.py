from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from EnglishClass import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('education/', include('education.urls')),
    path('people/', include('people.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
