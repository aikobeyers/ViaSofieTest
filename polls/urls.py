from django.conf.urls import url

from polls import views as home_views
from polls import views as about_views

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^about/', about_views.about, name='about'),
]
