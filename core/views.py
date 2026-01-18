# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import send_test_email  # Celery task example

class TestAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, DjangoOps!"})

    def post(self, request):
        # Example: trigger a Celery task
        send_test_email.delay()
        return Response({"message": "Task sent to Celery!"}, status=status.HTTP_202_ACCEPTED)
