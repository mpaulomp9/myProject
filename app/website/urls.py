from django.urls import path
from website.views import home, news

urlpatterns = [
    path('noticias/', news, name='news'),
    path('', home, name='home'),
]
