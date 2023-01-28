## Script to create a new calendar in google calendars

from cal_utils.cal_setup import get_calendar_service
from googleapiclient import errors

def create_calendar(summary, description, timezone):
    # Create a new calendar
    calendar = {
        'summary': summary,
        'description': description,
        'timeZone': timezone,
    }
    service = get_calendar_service()
    try:
        created_calendar = service.calendars().insert(body=calendar).execute()
    except errors.HttpError:
        print("Failed to create calendar")
        return 0

    print("Calendar created")
    return created_calendar['id']