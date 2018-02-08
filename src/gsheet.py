from src.time_operations import *
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import helpers


# returns a gspread object
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


# main function - accepts events and manages its addition to the sheet
def event_handler(sheet, event):
    title = event.month + ' ' + event.year
    if not check_week(sheet, event):
        month = sheet.add_worksheet(title=title, rows='20', cols='20')
        # fill month with weeks

    else:
        month = sheet.worksheet('title')


def check_week(sheet, event):
    worksheet_list = sheet.worksheets()
    formatted_date = event.month + event.year

    if formatted_date in worksheet_list:
        return True
    else:
        return False


def create_month(sheet, month):
    first_monday = first_monday_month(month)
    week_list = []
    for i in range(number_mondays_month(month)):
        week_list.append(full_week(first_monday + timedelta(days=7 * i)))

    event_month = first_monday_month(month).strftime('%B')
    worksheet = sheet.add_worksheet(title=event_month, rows="200", cols="30")

    '''
    position = 1
    for week in week_list:
        for day in week:
            worksheet.update_cell(1, position, day.strftime('%d/%m/%y'))
            position += 1
    '''

    for idx, week in enumerate(week_list):
        for jdx, day in enumerate(week):
            row = (idx + 1) + 12 * idx
            worksheet.update_cell(row, jdx+1, day.strftime('%d/%m/%y'))

    return worksheet


def write_event(obj, data):
    obj.update_cell(1, 1, data)
    return True


def delete_event(obj):
    obj.update_cell(1, 1, '')
    pass



