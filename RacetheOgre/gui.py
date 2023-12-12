import pygame
import sys
import day
from game import Game
from athlete import Athlete

class GameGUI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Race The Ogre")
        self.clock = pygame.time.Clock()

    def draw_day(self, day):
        font = pygame.font.Font(None, 36)
        text_training_plan = font.render(f"Training Plan: {day.training_plan}", True, (0, 0, 0))
        text_fitness_benefit = font.render(f"Fitness Benefit: {day.fitness_benefit}", True, (0, 0, 0))
        text_injury_risk = font.render(f"Injury Risk: {day.injury_risk}", True, (0, 0, 0))

        self.screen.blit(text_training_plan, (10, 10))
        self.screen.blit(text_fitness_benefit, (10, 50))
        self.screen.blit(text_injury_risk, (10, 90))

    def play_game(self, days):
        for day in days:
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        # Switch to resting state when the user presses SPACE
                        running = False

                # Draw the GUI
                self.screen.fill((255, 255, 255))  # White background
                self.draw_day(day)  # Draw the day information

                pygame.display.flip()
                self.clock.tick(60)  # 60 frames per second

        pygame.quit()
        sys.exit()


# Example usage:
if __name__ == "__main__":
    gui = GameGUI(800, 600)
    player_athlete = Athlete(speed=5.0, threshold=160, vo2max=55)
    opponent_athlete = Athlete(speed=4.5, threshold=155, vo2max=50)
    game = Game(player_athlete, opponent_athlete)
    gui.play_game(game.create_days_array)