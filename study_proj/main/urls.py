from django.conf.urls import include, url
from main.views import MainView, AddView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^add_(?P<card_type>[\w{3}])', AddView.as_view(), name='add')
]
