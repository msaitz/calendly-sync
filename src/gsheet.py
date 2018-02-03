from src.time_operations import get_next_monday, get_full_week
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import helpers


def authenticate():
    scope = ['https://spreadsheets.google.com/feeds']
    file = helpers.json_path('client_secret.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(file, scope)
    client = gspread.authorize(credentials)
    return client


def open_sheet(obj, name, worksheet=None):
    sheet = obj.open(name)
    if worksheet:
        sheet = sheet.worksheet(worksheet)
    return sheet


def write_event(obj, data):
    obj.update_cell(1, 1, data)
    return True


def delete_event(obj):
    obj.update_cell(1, 1, '')
    pass

'''
class Gsheet:
    def __init__(self, name, worksheet=None):
        scope = ['https://spreadsheets.google.com/feeds']
        file = helpers.json_path('client_secret.json')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(file, scope)
        self.client = gspread.authorize(credentials)
        self.sheet = self.open_sheet(name, worksheet=None)

    def open_sheet(self, name, worksheet=None):
        sheet = self.client.open(name)
        if worksheet:
            sheet = sheet.worksheet(worksheet)
        return sheet

    def write_event(self):
        return self.client

    def delete_event(self):
        test = self.write_event()

    def create_week(self):
        print()
'''

