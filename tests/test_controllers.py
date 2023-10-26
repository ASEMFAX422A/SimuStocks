# SimuApp/tests/test_controllers.py
import unittest
from flask import url_for
from app import create_app

class TestControllers(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
