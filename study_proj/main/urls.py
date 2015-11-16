from django.conf.urls import include, url
from main.views import MainView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
]
