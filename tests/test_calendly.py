import unittest
from lib import calendly


class TestCalendly(unittest.TestCase):

    def setUp(self):
            self.w = calendly.CalendlyEvent()

    def test_echo(self):
        self.assertTrue(self.w.echo())

    def test_get_subscriptions(self):
        self.assertTrue(self.w.get_subscriptions())

    def test_getters(self):
        with open('datafiles/raw_data') as content:
            data = content.read()

        self.w.add_event(data)
        self.assertEqual(self.w.name, 'Test McTest')
        self.assertEqual(self.w.time, '10:15')
        #self.assertEqual(self.w.time_index, 7)
        #self.assertEqual(self.w.date, 'Thursday, February 1, 2018')
        self.assertEqual(self.w.event_type, 'mobilehandover')


if __name__ == '__main__':
    unittest.main()



