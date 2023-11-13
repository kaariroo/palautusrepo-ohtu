from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.stats = []
        self.sorted_list = []

    def sort_by_points(self, player):
        return player.points

    def top_scorers_by_nationality(self, nationality):
        for player in self.reader.get_players():
            if player.nationality == nationality:
                self.stats.append(player)
        self.sorted_list = sorted(
            self.stats,
            reverse=True,
            key = self.sort_by_points
            )
        return self.sorted_list
        

