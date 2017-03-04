import unittest
from lib.math import sqrt

class TestSmoke (unittest.TestCase):

    def test_sqrt (self):
        self.assertEqual (sqrt (9), 3)
        self.assertRaises (ValueError, sqrt, 'a')
