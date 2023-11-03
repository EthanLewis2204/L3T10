from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_wandering_foot, name='the_wandering_foot'),
    path('gigs/', views.gigs, name='gigs'),
    path('songs/', views.songs, name='songs'),
]