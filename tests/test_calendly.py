from model import calendly
import unittest
import helpers


class TestCalendly(unittest.TestCase):
    def setUp(self):
            self.event = calendly.CalendlyEvent()

    def test_echo(self):
        self.assertTrue(self.event.echo())

    def test_get_subscriptions(self):
        self.assertTrue(self.event.get_subscriptions())

    def test_getters(self):
        self.event.add_event(helpers.load_file('raw_data'))
        self.assertEqual(self.event.name, 'Test McTest')
        self.assertEqual(self.event.time, '10:15')
        self.assertEqual(self.event.day, '01')
        self.assertEqual(self.event.month, '02')
        self.assertEqual(self.event.year, '18')
        self.assertEqual(self.event.time_index, 1)
        self.assertEqual(self.event.event_type, 'mobilehandover')


if __name__ == '__main__':
    unittest.main()



