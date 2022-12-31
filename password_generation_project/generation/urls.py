from django.urls import path
from .views import home
from .views import password
from .views import about


urlpatterns = [
    path('', home, name='home'),
    path('password', password, name='password'),
    path('about', about)
]