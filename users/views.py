from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import decorators, permissions
import os


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.AllowAny])
def test(request):
    return Response("Hello world!")


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def test_auth(request):
    return Response("test auth")
