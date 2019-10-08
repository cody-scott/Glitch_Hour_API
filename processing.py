import requests
import json
import re
from collections import OrderedDict
import google_service_api

import logging
import datetime


def _process_value(value):
    if value == '':
        return None
    else:
        return value


def log_hours(json_data):

    spreadsheet_id = json_data.get('sheet_id')
    sheet_range = 'HourTracking!A:G'
    date = json_data.get('date', None)
    data = json_data.get('data', [])

    service = google_service_api.get_service()
    sheet = service.spreadsheets()

    data[0] = _process_value(data[0])
    data[1] = _process_value(data[1])
    data[2] = _process_value(data[2])
    data[3] = _process_value(data[3])

    c_time = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")

    out_data = [
        c_time,
        date,
        data[1],
        data[2],
        data[0],
        data[3],
    ]

    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=sheet_range,
        valueInputOption='USER_ENTERED',
        body={
            'values': [out_data]
            }
    ).execute()

    pass


