from src import gsheet
import unittest


class TestGsheet(unittest.TestCase):
    def setUp(self):
        self.sheet = gsheet.Gsheet()

    def test_read_write_value(self):
        sheet = self.sheet.client.open('py test')
        test_ws = sheet.worksheet('test')
        test_ws.update_cell(3, 3, 'yeah')
        self.assertEqual(test_ws.cell(3, 3,).value, 'yeah')

    def create_month(self):
        pass


if __name__ == '__main__':
    unittest.main()
