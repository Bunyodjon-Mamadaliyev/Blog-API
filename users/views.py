from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get', 'put'], url_path='users/me')
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# JWT Token olish va yangilash uchun View
class LoginView(TokenObtainPairView):
    """Tizimga kirish (JWT token olish)"""
    permission_classes = [permissions.AllowAny]

class RefreshTokenView(TokenRefreshView):
    """Tokenni yangilash"""
    permission_classes = [permissions.AllowAny]
