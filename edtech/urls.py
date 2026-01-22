from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import chatbot_api

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    # Accounts (register + user)
    path("api/auth/", include("apps.accounts.urls")),

    # Token endpoints
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Courses
    path("api/", include("apps.courses.urls")),

    # Quizzes
    path("api/quizzes/", include("apps.quizzes.urls")),

    # Chatbot API (direct)
    path("api/chatbot/", include("apps.chatbot.urls")),

]


# ✅ ADD THIS
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )