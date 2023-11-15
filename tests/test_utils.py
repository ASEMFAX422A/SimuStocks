import unittest
from unittest.mock import Mock
from SimuApp.app.utils import safe_cast, is_valid_object_id


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.mock_app = Mock()

    def test_safe_cast(self):
        result = safe_cast("1", int, self.mock_app)
        self.assertEqual(result, 1)

        result = safe_cast("abc", int, self.mock_app, default=0)
        self.assertEqual(result, 0)

    def test_valid_object_id(self):
        self.assertTrue(is_valid_object_id("5f5b5f7e1c9d440000c7877e"))
        self.assertFalse(is_valid_object_id("invalid_id"))
        self.assertFalse(is_valid_object_id(""))
        self.assertFalse(is_valid_object_id(None))
        self.assertFalse(is_valid_object_id("5f5b5f7e1c9d440000c78"))
