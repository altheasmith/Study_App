from django.conf.urls import include, url
from main.views import MainView, GetCard

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^(?P<card_type>[\w]{5})card$', GetCard.as_view(), name='getcard'),
]
