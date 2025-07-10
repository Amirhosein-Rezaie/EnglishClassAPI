from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from EnglishClass import settings
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('education/', include('education.urls')),
    path('people/', include('people.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(), name='swagger_ui'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
