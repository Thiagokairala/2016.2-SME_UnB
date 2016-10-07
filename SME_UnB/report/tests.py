from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import unittest

class TestReportView(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_getting_page_report(self):
        response = self.client.post(
            '/reports/report/',
            {"username": 'temporary', 'password': 'temporary' }
        )

        self.assertEqual(200, response.status_code)

    def test_getting_wrong_page_report(self):
        response = self.client.post(
            '/reports/reports/',
            {"username": 'temporary', 'password': 'temporary' }
        )

        self.assertEqual(404, response.status_code)

    def test_getting_pdf(self):
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get('/reports/open_pdf/')
        print(response.status_code)

        self.assertEqual(200, response.status_code)
