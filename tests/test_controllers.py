# /tests/test_controllers.py

from SimuApp.app import create_app  # Pfad zur create_app Funktion
from SimuApp.app.models import User
from mongomock import MongoClient
from flask import url_for
from flask_login import login_user, logout_user
import unittest


class TestControllers(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.app.config["SERVER_NAME"] = "localhost.de:5000"
        self.client = self.app.test_client()
        self.user = User(firstname="Test", lastname="User", email="test@user.com")

    def test_index_route(self):
        with self.app.app_context():
            response = self.client.get(url_for("main.index"))
        self.assertEqual(response.status_code, 200)

    def test_logging_routes(self):
        routes_to_test = [
            "main.produce_debug",
            "main.produce_info",
            "main.produce_warning",
            "main.produce_error",
            "main.produce_critical",
        ]

        for route in routes_to_test:
            with self.subTest(route=route):
                with self.app.app_context():
                    with self.app.test_request_context():
                        # Test für authentifizierten Benutzer
                        login_user(self.user)
                        response = self.client.get(url_for(route))
                        self.assertEqual(response.status_code, 302)
                        # TODO: check if we realy produce log entry

                        # Test für anonymen Benutzer
                        logout_user()
                        response = self.client.get(url_for(route))
                        self.assertEqual(response.status_code, 302)
                        # TODO: check if we realy produce log entry
