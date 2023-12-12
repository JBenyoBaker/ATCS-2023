class Athlete:
    def __init__(self, speed, threshold, vo2max):
        self.speed = speed
        self.threshold = threshold
        self.vo2max = vo2max
        self.state = "resting"  # Initial state

    def display_info(self):
        print(f"Athlete Information:\nSpeed: {self.speed} m/s\nThreshold: {self.threshold} bpm\nVO2 Max: {self.vo2max} ml/kg/min\nState: {self.state}")

    def start_training(self):
        if self.state == "resting":
            self.state = "training"
            print("Athlete started training.")
        else:
            print("Athlete can only start training from the resting state.")

    def start_racing(self):
        if self.state == "resting":
            self.state = "racing"
            print("Athlete started racing.")
        else:
            print("Athlete can only start racing from the resting state.")

    def rest(self):
        if self.state == "training" or self.state == "racing":
            self.state = "resting"
            print("Athlete is resting.")
        else:
            print("Athlete is already resting.")

    # Getter for speed
    def get_speed(self):
        return self._speed

    # Setter for speed
    def set_speed(self, speed):
        self._speed = speed

    # Getter for threshold
    def get_threshold(self):
        return self._threshold

    # Setter for threshold
    def set_threshold(self, threshold):
        self._threshold = threshold

    # Getter for vo2max
    def get_vo2max(self):
        return self._vo2max

    # Setter for vo2max
    def set_vo2max(self, vo2max):
        self._vo2max = vo2max

# Example usage:
athlete1 = Athlete(speed=5.0, threshold=160, vo2max=55)
athlete1.display_info()

athlete1.start_training()
athlete1.display_info()

athlete1.start_racing()
athlete1.display_info()

athlete1.rest()
athlete1.display_info()