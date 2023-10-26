# /tests/test_controllers.py

from SimuApp.app import create_app  # Pfad zur create_app Funktion
from flask import url_for
import unittest


class TestControllers(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        self.client = self.app.test_client()

    def test_index_route(self):
        with self.app.app_context():
            response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)

