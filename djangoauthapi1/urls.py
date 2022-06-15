from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/schema/', SpectacularAPIView.as_view(),name='api_schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='api_schema'),name='api_docs'),
]
