from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegistrationSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        token = Token.objects.get(user=new_user)
        return Response({"R": token.key})


class LogoutView(APIView):
    def post(self, request):
        token = Token.objects.get(user=request.user).delete()
        return Response({"R": "DELETED"})
