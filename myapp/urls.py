from django.urls import path

from . import views

urlpatterns =[
    path('', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('social/', views.social, name='social'),
]