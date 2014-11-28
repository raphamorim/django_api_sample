# coding: utf-8

from django.test import TestCase

# from django.utils import unittest

# Create your tests here.

class RoutesTest(TestCase):

    def test_get_all_games_data(self):
        # 200 if route exists
        response = self.client.get('/game/')
        self.assertEqual(response.status_code, 200)

    def test_get_game_by_especified_category(self):
        # 200 if game exists
        response = self.client.get('/game/category/')
        self.assertEqual(response.status_code, 200)

        # 404 if game not exists
