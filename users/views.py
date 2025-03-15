from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework import viewsets
from .permissions import IsOwnerOrStaff

class UserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class IsAdminUserOrIsItself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
permission_classes = [IsAdminUser & IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."})


class UserProfileDetailView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, pk):
        article = get_object_or_404(UserProfile, pk=pk)
        self.check_object_permissions(request, article)
        serializer = UserProfileSerializer(article)
        return Response(serializer.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrStaff]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return UserProfile.objects.filter(user=self.request.user)
        return UserProfile.objects.all()