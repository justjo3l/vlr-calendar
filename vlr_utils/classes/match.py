class Match:
    def __init__(self, time, length, team1, team2, round, stage):
        self.time = time
        self.length = length
        self.team1 = team1
        self.team2 = team2
        self.round = round
        self.stage = stage

    def print_match(self):
        print("Match time: " + str(self.time))
        print("Match length: " + str(self.length))
        print("Team 1: " + self.team1.name)
        print("Team 2: " + self.team2.name)
        print("Round: " + self.round)
        print("Stage: " + self.stage)