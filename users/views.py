from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer


# Ro‘yxatdan o‘tish uchun View
class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='auth/register')
    def register(self, request):
        """Foydalanuvchini ro‘yxatdan o‘tkazish"""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created", "user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Foydalanuvchini boshqarish uchun ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get', 'put'], url_path='users/me')
    def me(self, request):
        """Foydalanuvchi o‘z profilini ko‘rish yoki yangilash"""
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
