from cal_utils.cal_setup import get_calendar_service

def list_calendars():
   service = get_calendar_service()
   # Call the Calendar API
   print('Getting list of calendars')
   calendars_result = service.calendarList().list().execute()

   calendars = calendars_result.get('items', [])

   if not calendars:
       print('No calendars found.')
    
   return calendars
