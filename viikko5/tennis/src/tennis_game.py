class TennisGame:
    def __init__(self, player1_name, player2_name, draw, matchpoint):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.draw = draw
        self.matchpoint = matchpoint
        

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
        
        if self.player1_score == self.player2_score:
            self.draw = True
        else:
            self.draw = False
        if self.draw == False:
            if self.player1_score >= 4 or self.player2_score >=4:
                self.matchpoint = True
            else:
                self.matchpoint = False

    def analyze_draw(self, player_score):
        if player_score == 0:
            score = "Love-All"
        elif player_score == 1:
            score = "Fifteen-All"
        elif player_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
        
    def analyze_matchpoint_difference(self, player1_score, player2_score):
        point_difference = player1_score - player2_score
        if point_difference == 1:
                score = "Advantage player1"
        elif point_difference == -1:
            score = "Advantage player2"
        elif point_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def analyze_situation(self, player1_score, player2_score):
        score = ""
        player_counter = 0
        players_in_game = [player1_score, player2_score]
        for player_score in players_in_game:
            if player_score == 0:
                score = score + "Love"
            elif player_score == 1:
                score = score + "Fifteen"
            elif player_score == 2:
                score = score + "Thirty"
            elif player_score == 3:
                score = score + "Forty"
            if player_counter == 0:
                score = score + "-"
            player_counter += 1
        return score


    def get_score(self):
        score = ""
        if self.draw:
            score = self.analyze_draw(self.player1_score)
            
        elif self.matchpoint:
            score = self.analyze_matchpoint_difference(self.player1_score, self.player2_score)
            
        else:
            score = self.analyze_situation(self.player1_score, self.player2_score)

        return score
