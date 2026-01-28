import os
from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()

    username = os.environ.get("ADMIN_USERNAME")
    email = os.environ.get("ADMIN_EMAIL")
    password = os.environ.get("ADMIN_PASSWORD")

    if not username or not password:
        return "Missing admin env vars"

    if User.objects.filter(username=username).exists():
        return "Admin already exists"

    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )

    return "Admin created"
