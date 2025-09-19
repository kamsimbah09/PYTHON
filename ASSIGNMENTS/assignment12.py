class Games:
    def _init_(self, sport_name, team_number, team_players):
        self.sport = sport_name
        self.team_number = team_number
        self.team_players = team_players_per_team

    def show(self):
        print(f{self.sport_name}"is my favourite to play") 
         print(f"We are "{self.team_number}"in my team") 
          print(f"There are"{self.team_players_per_team}"teams in total") 

football = Games("Football","11","2") 
basketball = Games("Basketball","6","2") 
Rugby = Games("Rugby","1","2") 
table_tennis = Games("Table Tennis","1","2")          

football.show()
basketballball.show()
rugby.show()
table_tennis.show()