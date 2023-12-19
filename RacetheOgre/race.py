class Race:
    def __init__(self, athlete1, athlete2):
        self.athlete1 = athlete1
        self.athlete2 = athlete2

    def simulate_race(self):
        print("Let the race begin!")

        player_speed = self.athlete1.speed / 2
        computer_speed = self.athlete2.speed / 2

        player_distance = 0
        computer_distance = 0

        while player_distance < 1000 and computer_distance < 1000:
            print("\nRace Status:")

            #calculate player's instantaneous velocity in meters per second based off of their vo2max, threshold heart rate, and a estimation of what percentage of peak speed they are at 
            player_speed = (2 - (player_speed/ (self.athlete1.get_threshold() * 3 / self.athlete1.get_vo2max()))) * player_speed
            #calculate player's distance traveled
            player_distance += player_speed * 10

            #calculate computer's instantaneous velocity in meters per second based off of their vo2max, threshold heart rate, and a estimation of what percentage of peak speed they are at 
            computer_speed = (2 - (computer_speed / (self.athlete2.get_threshold() * 3 / self.athlete2.get_vo2max()))) * computer_speed
            #calculate computer's distance traveled
            computer_distance += computer_speed * 10
            
            print(f"Player Speed: {player_speed} Distance: {player_distance} | Computer Speed: {computer_speed} Distance: {computer_distance}")

            try:
                choice = input("Enter 'f' to go faster, 's' to go slower:").lower()

                if choice == 'f':
                    player_speed += 2
                elif choice == 's':
                    player_speed -= 2
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

            #AI determining whether or not the computer should go faster or slower
            #Basically is saying if the computer is running less than 100% of their maintainable speed then speed up otherwise slow down
            if (computer_speed / (self.athlete2.get_threshold() * 2.5 / self.athlete2.get_vo2max())) * computer_speed < 1:
            #calculate computer's distance traveled < 1:
                computer_speed += 2
            else:
                computer_speed -= 2
        
        if player_distance >= 1000:
            print("player wins")
        else:
            print("computer wins")
