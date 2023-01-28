from datetime import datetime, timedelta
from cal_utils.cal_setup import get_calendar_service


def create_event(calendar_id, summary, description, start, length, timezone):
   service = get_calendar_service()

   start_d = start
   start_d = datetime(start_d.year, start_d.month, start_d.day, start_d.hour, start_d.minute)
   start = start_d.isoformat()
   end = (start_d + timedelta(minutes=length)).isoformat()

   event_result = service.events().insert(calendarId=calendar_id,
       body={
           "summary": summary,
           "description": description,
           "start": {"dateTime": start, "timeZone": timezone},
           "end": {"dateTime": end, "timeZone": timezone},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

   return 1