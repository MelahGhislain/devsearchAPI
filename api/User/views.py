from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile

# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView():
    pass


class ProfileView(GenericAPIView):
    serializer_class = ProfileSerializer
    
    def get(self, request):
        try:
            profile = Profile.objects.all()
        except Exception:
            return Response({"Error": "profile not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def post(self, request):
        print(request.user.username)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
