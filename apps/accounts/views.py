from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username_or_email = request.data.get("username")
        password = request.data.get("password")

        # Basic validation
        if not username_or_email or not password:
            return Response(
                {"detail": "Username (or email) and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # If user provided an email, resolve to username
        if "@" in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username_or_email = user.username
            except User.DoesNotExist:
                return Response({"detail": "Invalid credentials"}, status=400)

        user = authenticate(username=username_or_email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }
            )

        return Response({"detail": "Invalid credentials"}, status=400)
