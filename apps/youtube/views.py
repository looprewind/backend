from django.http import HttpResponse
from rest_framework import generics

from .models import YoutubeURL
from .serializers import YoutubeURLSerializer


class YoutubeURLListView(generics.ListCreateAPIView):
    queryset = YoutubeURL.objects.all()
    serializer_class = YoutubeURLSerializer
    ordering_fields = ["created_at"]
    # a good practice would be paginate the results


def test(request):
    return HttpResponse('Hi there Relief employee!')
