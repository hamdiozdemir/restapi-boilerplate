"""
Simple test for health check.
"""

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CORE_URL = reverse('core:index')


class CheckCoreAPITest(TestCase):
    """Testcase for core api."""

    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        """Test Check."""
        response = self.client.get(CORE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['check'], 'ok')
