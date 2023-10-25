import unittest
from unittest.mock import Mock
from SimuApp.app.utils import safe_cast

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.mock_app = Mock()

    def test_safe_cast(self):
        result = safe_cast('1', int, self.mock_app)
        self.assertEqual(result, 1)

        result = safe_cast('abc', int, self.mock_app, default=0)
        self.assertEqual(result, 0)