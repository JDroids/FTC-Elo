class Team:
    ranking = 1000
    games_played = 0
    total_opponents_rating = 0
    score_differences = 0

    def __init__(self, team_number: int, team_name: str):
        self.team_number = team_number
        self.team_name = team_name
        
    def update_ranking(self, alliance_score: int, opponent_alliance_score: int, teammate, opponent_1, opponent_2):
        opponent_alliance_average_rating = (opponent_1.ranking + opponent_2.ranking) / 2

        self.games_played += 1
        self.total_opponents_rating += opponent_alliance_average_rating 

        self.score_differences += alliance_score - opponent_alliance_score

        self.ranking = round((self.total_opponents_rating + (self.score_differences)) / self.games_played)
