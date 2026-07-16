# Project: csv-parser-analyzer-class-based

def sumarize(analyzer):
    print(f"Top Score: {analyzer.findTopScore()}")
    print(f"Average Score: {analyzer.findMeanScore()}")
    print(f"Top Player: {analyzer.findTopPlayer()}")
    print(f"Average Level: {analyzer.findMeanLevel()}")

class DataAnalyzer:
    def __init__(self):
        self.headers = []
        self.players = []
        with open("./players.csv", "r") as file:
            for index, line in enumerate(file):
                if index == 0:
                    self.headers = line.strip().split(",")
                else:
                    self.players.append(dict(zip(self.headers, line.strip().split(","))))
        self.scores = [int(player["score"]) for player in self.players]
    
    def findTopScore(self):
        return max(self.scores)

    def findMeanScore(self):
        return round(sum(self.scores) / len(self.scores), 2)

    def findTopPlayer(self):
        topScore = self.findTopScore()
        for playerIndex, player in enumerate(self.players):
            if self.scores[playerIndex] == topScore:
                return player["name"]
            
    def findMeanLevel(self):
        levels = [int(player["level"]) for player in self.players]
        return round(sum(levels) / len(levels), 2)


analyzer = DataAnalyzer()
sumarize(analyzer)
