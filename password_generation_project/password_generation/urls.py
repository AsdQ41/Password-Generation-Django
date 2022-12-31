from django.urls import path, include



urlpatterns = [
    path('', include('generation.urls')),
    path('password', include('generation.urls'))
]
