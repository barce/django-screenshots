from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.ScreenshotViewSet)

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^screenshots/$', views.ScreenshotList.as_view()),
    url(r'^screenshots/(?P<pk>[0-9]+)/$', views.ScreenshotDetail.as_view()),
    url(r'^screenshot_search/(?P<url>.+)/$', views.ScreenshotSearch.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
