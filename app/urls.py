from django.urls import path
from . import views


urlpatterns = [
    path('home',views.index, name='home' ),
    path('login',views.login, name='login'),
    path('currency', views.currency, name='currency'),
    path('rating', views.rating, name='rating'),
    path('registration', views.registration, name='registration'),
]