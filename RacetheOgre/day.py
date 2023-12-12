class Day:
    def __init__(self, training_plan, fitness_benefit, injury_risk):
        self.training_plan = training_plan
        self.fitness_benefit = fitness_benefit
        self.injury_risk = injury_risk

    def display_info(self):
        print("Day Information:")
        print(f"Training Plan: {self.training_plan}")
        print(f"Fitness Benefit: {self.fitness_benefit}")
        print(f"Injury Risk: {self.injury_risk}")

#  Example usage:
# day1 = Day(training_plan="Strength Training", fitness_benefit=3, injury_risk=2)
# day1.display_info()