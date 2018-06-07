def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

class Team:
    ranking = 1000

    def __init__(self, team_number: int, team_name: str):
        self.team_number = team_number
        self.team_name = team_name

    def expected(self, teammate, opponent_1, opponent_2):
        print(self.team_number, self.team_name, 'Expected', (1 + 10 ** (((self.ranking + teammate.ranking) - (opponent_1.ranking + opponent_2.ranking)) / 400)))
        return (((self.ranking + teammate.ranking) - (opponent_1.ranking + opponent_2.ranking)) / 400)

    def update_ranking(self, alliance_score: int, teammate, opponent_1, opponent_2, k=32):
        change = (alliance_score - (self.expected(teammate, opponent_1, opponent_2) + teammate.expected(self, opponent_1, opponent_2)))
        
        self.ranking = clamp(change, self.ranking - k, self.ranking + k)

        self.ranking = round(self.ranking)