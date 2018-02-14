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
        event_create = CalendlyEvent()
        event_create.add_event(helpers.load_file('raw_data2'))
        event_cancel = CalendlyEvent()
        event_cancel.add_event(helpers.load_file('raw_data_cancel'))

        # add event
        event_handler(self.sheet, event_create)
        # remove event
        event_handler(self.sheet, event_cancel)


if __name__ == '__main__':
    unittest.main()
