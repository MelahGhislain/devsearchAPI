from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view())
]
