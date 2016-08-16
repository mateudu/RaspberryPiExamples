from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^display-text/', views.display_text, name= 'display-text'),
]