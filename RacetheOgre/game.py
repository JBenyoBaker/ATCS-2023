from athlete import Athlete
from day import Day
from race import Race
#rom gui import GameGUI 

class Game:
    def __init__(self, player_athlete, opponent_athlete):
        self.player_athlete = player_athlete
        self.opponent_athlete = opponent_athlete

        #make a set of days which have fitness benefits and injury risks
        training_plan = self.create_days_array(player_athlete)

    def display_players_info(self):
        print("Player Athlete:")
        self.player_athlete.display_info()
        print("\nOpponent Athlete:")
        self.opponent_athlete.display_info()

    def create_days_array(self, Athlete):
        days_array = []
    
        # Assuming different training benefits for each attribute
        speed_day = Day(training_plan="Speed Training", fitness_benefit= 2, injury_risk=3)
        threshold_day = Day(training_plan="Threshold Training", fitness_benefit= 1.5, injury_risk=2)
        vo2max_day = Day(training_plan="VO2 Max Training", fitness_benefit= 1.8, injury_risk=4)
    
        days_array.extend([speed_day, threshold_day, vo2max_day])
        return days_array

def main():
    race_athlete1 = Athlete(speed=10, threshold=160, vo2max=55, injury_risk=2)
    race_athlete2 = Athlete(speed=9, threshold=155, vo2max=52, injury_risk=2)
    game = Game(race_athlete1, race_athlete2)

    while True:
        choice = input("Choose an option:\n1. Do a Training Day\n2. Simulate a Race\n3. Take a Rest Day\n4. Quit\n")

        if choice == '1':
            print("Doing a Training Day!")
            # Add training day logic here
            race_athlete1.set_speed(race_athlete1.get_speed() + 0.3)
            race_athlete1.set_threshold(race_athlete1.get_threshold() + 5)
            race_athlete1.set_vo2max(race_athlete1.get_vo2max() + 1)
            race_athlete1.set_injury_risk(race_athlete1.get_injury_risk() - 1)
        elif choice == '2':
            race = Race(race_athlete1, race_athlete2)
            race.simulate_race()
        elif choice == '3':
            print("Taking a Rest Day!")
            # Add rest day logic here
            race_athlete1.set_injury_risk(race_athlete1.get_injury_risk() - 1)
        elif choice == '4' or race_athlete1.get_injury_risk == 10:
            print("Game Over. Exiting the program.")
            exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()