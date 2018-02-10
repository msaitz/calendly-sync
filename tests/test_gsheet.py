from src.gsheet import *
from datetime import datetime
from src.calendly import CalendlyEvent
import unittest
import helpers


class TestGsheet(unittest.TestCase):
    def setUp(self):
        self.client = authenticate()
        self.sheet = open_sheet(self.client, 'py test')
        self.worksheet = open_sheet(self.client, 'py test', 'test')

        year = datetime.now().year
        self.day1 = datetime(year, 1, 1).strftime('%d/%m/%y')
        self.day2 = datetime(year, 1, 22).strftime('%d/%m/%y')
    '''
    def test_read_write_value(self):
        write_event(self.worksheet, 'Miguel')
        self.assertEqual(self.worksheet.cell(1, 1, ).value, 'Miguel')
        delete_event(self.worksheet)

    def test_add_workshet_write_month(self):
        new_worksheet = create_month(self.sheet, 1)
        worksheets = self.sheet.worksheets()
        self.assertTrue(new_worksheet in worksheets)

        self.assertEqual(new_worksheet.cell(1, 1).value, self.day1)
        self.assertEqual(new_worksheet.cell(40, 1).value, self.day2)

        self.sheet.del_worksheet(new_worksheet)
    '''

    def test_event_handler(self):
        event = CalendlyEvent()
        event.add_event(helpers.load_file('raw_data'))

        for i in range(12):

            event.change_date(datetime(2018, 1 + i, first_monday_month(1 + i).day + 7))
            event_handler(self.sheet, event)


if __name__ == '__main__':
    unittest.main()
