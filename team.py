class Team:
    ranking = 1000

    def __init__(self, team_number: int, team_name: str):
        self.team_number = team_number
        self.team_name = team_name

    def expected(self, teammate, opponent_1, opponent_2):
        return 1 / (1 + 10 ** (((self.ranking + teammate.ranking) - (opponent_1.ranking + opponent_2.ranking)) / 400))

    def update_ranking(self, alliance_score: int, teammate, opponent_1, opponent_2, k=(1)):
        self.ranking += k * (alliance_score - (self.expected(teammate, opponent_1, opponent_2) + teammate.expected(self, opponent_1, opponent_2)))
        self.ranking = round(self.ranking)