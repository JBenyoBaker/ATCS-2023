from athlete import Athlete
import day
from gui import GameGUI 

class Game:
    def __init__(self, player_athlete, opponent_athlete):
        self.player_athlete = player_athlete
        self.opponent_athlete = opponent_athlete

        #make a set of days which have fitness benefits and injury risks
        training_plan = self.create_days_array()

    def display_players_info(self):
        print("Player Athlete:")
        self.player_athlete.display_info()
        print("\nOpponent Athlete:")
        self.opponent_athlete.display_info()

    def simulate_race(self):
        print("\nSimulating race...")
        self.player_athlete.start_racing()
        self.opponent_athlete.start_racing()

        # Simulate the race based on some criteria (you can customize this)
        player_finish_time = 1 / player_athlete.get_threshold() * player_athlete.get_vo2max() + player_athlete.get_speed()
        opponent_finish_time = 1 / opponent_athlete.get_threshold() * opponent_athlete.get_vo2max() + opponent_athlete.get_speed()

        print("\nRace simulation results:")
        print(f"Player Athlete finished the race in {player_finish_time} seconds.")
        print(f"Opponent Athlete finished the race in {opponent_finish_time} seconds.")

        if player_finish_time < opponent_finish_time:
            print("Player Athlete wins!")
        elif player_finish_time > opponent_finish_time:
            print("Opponent Athlete wins!")
        else:
            print("It's a tie!")
    
    def create_days_array(Athlete):
        days_array = []
    
        # Assuming different training benefits for each attribute
        speed_day = day(training_plan="Speed Training", fitness_benefit=Athlete.speed * 2, injury_risk=3)
        threshold_day = day(training_plan="Threshold Training", fitness_benefit=Athlete.threshold * 1.5, injury_risk=2)
        vo2max_day = day(training_plan="VO2 Max Training", fitness_benefit=Athlete.vo2max * 1.8, injury_risk=4)
    
        days_array.extend([speed_day, threshold_day, vo2max_day])
        return days_array
    
    def run():
        # Example usage:
        training_plan = self.create_days_array(player_athlete)
        gui = GameGUI(800, 600)
        gui.play_game(training_plan)

player_athlete = Athlete(speed=5.0, threshold=160, vo2max=55)
opponent_athlete = Athlete(speed=4.5, threshold=155, vo2max=50)
game = Game(player_athlete, opponent_athlete)
game.display_players_info()
game.simulate_race()
game.run()