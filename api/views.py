from django.shortcuts import render
from api.models import Profile, User
from api.serializer import RegisterSerializer, UserSerializer, MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == "GET":
        context = f"Hey {request.User}, You are seeing a GET response"
        return Response({'response': context}, status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        text = request.POST.get("text")
        response = f"Hey {request.User}, your text is {text}"
        return Response({'response': response}, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content: {'message': 'Welcome to the social authentication application using react and django !'}
        return Response(content)
    

class GoogleView(APIView):

    def post(self, request):
        id_token = request.data.get("idToken")
        token = {'id_token': request.data.get('idToken')}
        decodedPayload = jwt.JWT().decode(id_token, None, None)
        email = decodedPayload['email']
        full_name = decodedPayload['name']
        imageURL = decodedPayload['picture']
        verified = decodedPayload['email_verified']
        username = email.split('@')[0]
        print("decoded Payload: ", decodedPayload)
        return {
            "message" : "got yeahhh"
        }
        

