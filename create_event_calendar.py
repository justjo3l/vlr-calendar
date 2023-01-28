from vlr_utils.find_event import find_event_matches
from cal_utils.create_calendar import create_calendar
from cal_utils.create_event import create_event
from cal_utils.cal_list import list_calendars
from cal_utils.delete_calendar import delete_calendar

timeZone = "Asia/Dubai"

def main():
    # Ask user for event ID
    event_id = input("Enter event ID: ")
    event = find_event_matches(event_id)

    for calendar in list_calendars():
        if calendar['summary'] == event.title:
            print("Calendar already exists")
            decider = input("Do you want to replace the existing calendar? (y/n): ")
            if decider == "y":
                calendar_id = calendar['id']
                delete_calendar(calendar_id)
                break
            else:
                return

    # Create a new calendar
    calendar_id = create_calendar(event.title, event.subtitle, timeZone)

    for match in event.matches:
        match_title = match.team1.name + " vs " + match.team2.name
        match_subtitle = match.round + " - " + match.stage
        match_start_time = match.time
        match_length = match.length

        # Create a new event
        create_event(calendar_id, match_title, match_subtitle, match_start_time, match_length, timeZone)

if __name__ == '__main__':
    main()