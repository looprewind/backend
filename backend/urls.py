from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.youtube.urls'), name="youtube"),
    path('admin/', admin.site.urls),
]
