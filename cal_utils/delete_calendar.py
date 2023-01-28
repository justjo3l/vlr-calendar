## Script to create a new calendar in google calendars

from cal_utils.cal_setup import get_calendar_service
from googleapiclient import errors

def delete_calendar(id):
    # Deletes a calendar
    service = get_calendar_service()
    try:
        created_calendar = service.calendars().delete(calendarId=id).execute()
    except errors.HttpError:
        print("Failed to create calendar")
        return 0

    print("Calendar deleted")
    return