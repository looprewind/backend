from django.urls import path

from .views import test, YoutubeURLListView


urlpatterns = [
    path('', YoutubeURLListView.as_view(), name='index'),
    path('test', test, name='test'),
]
