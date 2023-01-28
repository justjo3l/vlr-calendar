class Event:
    def __init__(self, title, subtitle, matches):
        self.title = title
        self.subtitle = subtitle
        self.matches = matches

    def print_event(self):
        print("Event title: " + self.title)
        print("Event subtitle: " + self.subtitle)
        for match in self.matches:
            match.print_match()
