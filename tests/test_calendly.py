import unittest
from lib import calendly


class TestCalendly(unittest.TestCase):

    def setUp(self):
            self.w = calendly.Calendly()

    def test_echo(self):
        self.assertTrue(self.w.echo())

    def test_get_key(self):
        self.assertIsNotNone(self.w.get_key())

    def test_get_subscriptions(self):
        self.assertIsNotNone(self.w.get_subscriptions())


if __name__ == '__main__':
    unittest.main()



