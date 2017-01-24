from .serializers import ScreenshotSerializer
from screenshots.models import Screenshot
from rest_framework import generics
import urllib.parse

class ScreenshotList(generics.ListCreateAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class ScreenshotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class ScreenshotSearch(generics.ListAPIView):
    serializer_class = ScreenshotSerializer

    def get_queryset(self):
        url = urllib.parse.unquote_plus(self.kwargs['url'])
        # add extra "/"
        url = url[0:6] + '/' + url[6:len(url)]
        print(url)
        return Screenshot.objects.filter(url=url)
