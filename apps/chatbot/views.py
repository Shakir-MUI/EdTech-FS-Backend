from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .groq_client import ask_groq

class ChatbotAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_message = request.data.get("message", "").strip()

        if not user_message:
            return Response(
                {"error": "No message provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        full_prompt = f"User: {user_message}"
        ai_reply = ask_groq(full_prompt)

        return Response({"response": ai_reply})
