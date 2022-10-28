from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserRegistrationView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


class UserProfileView(views.APIView):
    # queryset = UserModel.objects.all()
    # serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = UserModel.objects.all().get(username=request.user)
        serializer = UserProfileSerializer(qs)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserProfileSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
