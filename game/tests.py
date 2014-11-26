# coding: utf-8

from django.test import TestCase

# Create your tests here.

def test_get_list(self):
    # 200 if list exists
    response = self.client.get('127.0.0.1:8000/game/')
    self.assertEqual(response.status_code, 200)
