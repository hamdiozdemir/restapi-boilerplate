"""
Views for core app.
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class BasicAPIView(APIView):
    """Returns a basic response for health check."""

    def get(self, request, format=None):
        return Response({'check': 'ok'})
