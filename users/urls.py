from django.urls import path
from .views import RegisterView, CustomAuthToken, LogoutView, UserProfileCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserProfileCreateAPIView.as_view(), name='users')
]
