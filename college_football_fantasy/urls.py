from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^details/', include('data_grabber.urls', namespace='data_grabber')),
    url(r'^admin/', include(admin.site.urls)),
]
