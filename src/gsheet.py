from src.time_operations import get_next_monday, get_full_week
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import helpers


class Gsheet:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds']
        file = helpers.json_path('client_secret.json')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(file, scope)
        self.client = gspread.authorize(credentials)

    def write_event(self):
        return self.client

    def delete_event(self):
        test = self.write_event()

    def create_week(self):
        print()


