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
    if event.is_canceled:
        modify_event_cell(sheet, event, 'cancel')
        return
    modify_event_cell(sheet, event, 'add')


def modify_event_cell(sheet, event, action):
    if not is_worksheet_in_sheet(sheet, month=event.adjusted_month):
        month_worksheet = create_month(sheet, event.adjusted_month)
    else:
        month_string = datetime(datetime.now().year, event.adjusted_month, 1).strftime('%B')
        month_worksheet = sheet.worksheet(month_string)

    if action == 'cancel':
        cell_content = ''
    else:
        cell_content = event.event_type + ': ' + event.name

    event_location = month_worksheet.find(event.formatted_date)
    row = event_location.row + event.time_index + 1
    month_worksheet.update_cell(row, event_location.col, cell_content)


# may not be necessary
def write_new_worksheet_title(master_worksheet, title):
    master_worksheet.update_cell(1, 1, title)


def generate_event_week_title(sheet, event):

    pass


def get_latest_worksheet_week(sheet):
    worksheets = sheet.worksheets()
    obj_worksheets = [datetime.strptime(ws.title, '%b %d-%m-%y') for ws in worksheets if ws.title != 'Template']
    return max(obj_worksheets)


def is_worksheet_in_sheet(sheet, date=None, month=None):
    if month:
        target_title = datetime(datetime.now().year, month, 1).strftime('%B')
    else:
        target_title = date.strftime('%b %d-%m-%y')

    for worksheet in sheet.worksheets():
        if worksheet.title == target_title:
            return True
    return False


def is_month_in_sheet(sheet, month):
    worksheet_list = sheet.worksheets()
    month_str = datetime(datetime.now().year, month, 1).strftime('%B')

    for worksheet in worksheet_list:
        if worksheet.title == month_str:
            return True
    return False


def create_month(sheet, month):
    first_monday = first_monday_month(month)
    week_list = []
    for i in range(number_mondays_month(month)):
        week_list.append(full_week(first_monday + timedelta(days=7 * i)))

    event_month = first_monday_month(month).strftime('%B')
    worksheet = sheet.add_worksheet(title=event_month, rows="200", cols="6")

    for idx, week in enumerate(week_list):
        for jdx, day in enumerate(week):
            row = (idx + 1) + 24 * idx
            worksheet.update_cell(row, jdx+1, day.strftime('%d/%m/%y'))
    return worksheet

