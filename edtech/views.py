from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def chatbot_api(request):
    msg = request.data.get("message", "")

    # Dummy response for testing
    return Response({"response": f"You said: {msg}"})
