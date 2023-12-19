from fsm import FSM

class Athlete:
    def __init__(self, speed, threshold, vo2max, injury_risk):
        self.speed = speed
        self.threshold = threshold
        self.vo2max = vo2max
        self.injury_risk = injury_risk
        self.state = "resting"  # Initial state
        self.fsm = FSM('training')

        # Define transitions
        self.fsm.add_transition('do_training', 'resting', action=self.start_training, next_state='training')
        self.fsm.add_transition('enter_race', 'resting', action=self.start_racing, next_state='racing')
        self.fsm.add_transition('take_rest_day', 'resting', action=self.rest, next_state='resting')
        self.fsm.add_transition('do_training', 'training', action=self.start_training, next_state='training')
        self.fsm.add_transition('enter_race', 'training', action=self.start_racing, next_state='racing')
        self.fsm.add_transition('take_rest_day', 'training', action=self.rest, next_state='resting')
        self.fsm.add_transition('do_training', 'racing', action=self.start_training, next_state='training')
        self.fsm.add_transition('enter_race', 'racing', action=self.start_racing, next_state='racing')
        self.fsm.add_transition('take_rest_day', 'racing', action=self.rest, next_state='resting')

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
            #do the racing
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
        return self.speed

    # Setter for speed
    def set_speed(self, speed):
        self.speed = speed

    # Getter for threshold
    def get_threshold(self):
        return self.threshold

    # Setter for threshold
    def set_threshold(self, threshold):
        self.threshold = threshold

    # Getter for vo2max
    def get_vo2max(self):
        return self.vo2max

    # Setter for vo2max
    def set_vo2max(self, vo2max):
        self.vo2max = vo2max

    # Getter for injury_risk
    def get_injury_risk(self):
        return self.injury_risk

    # Setter for injury_risk
    def set_injury_risk(self, injury_risk):
        if injury_risk < 0:
            self._injury_risk = 0
        else:
            self._injury_risk = injury_risk


# Example usage:
athlete1 = Athlete(speed=5.0, threshold=160, vo2max=55, injury_risk=4)
athlete1.display_info()

athlete1.start_training()
athlete1.display_info()

athlete1.start_racing()
athlete1.display_info()

athlete1.rest()
athlete1.display_info()