from src.gsheet import *
import unittest
import datetime


class TestGsheet(unittest.TestCase):
    def setUp(self):
        self.client = authenticate()
        self.sheet = open_sheet(self.client, 'py test')
        self.worksheet = open_sheet(self.client, 'py test', 'test')

    def test_read_write_value(self):
        write_event(self.worksheet, 'Miguel')
        self.assertEqual(self.worksheet.cell(1, 1, ).value, 'Miguel')
        delete_event(self.worksheet)

    def test_add_workshet_write_month(self):
        new_worksheet = create_month(self.sheet, 1)
        worksheets = self.sheet.worksheets()
        self.assertTrue(new_worksheet in worksheets)

        self.assertEqual(new_worksheet.cell(1, 1).value, '01/01/18')
        self.assertEqual(new_worksheet.cell(1, 16).value, '22/01/18')

        self.sheet.del_worksheet(new_worksheet)


if __name__ == '__main__':
    unittest.main()
