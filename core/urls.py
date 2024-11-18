from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('services.urls')),
    path('api/v1/', include('appointments.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('specialists.urls')),
]
