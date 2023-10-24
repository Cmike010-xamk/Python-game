import pygame

###################################################
################## Class for score ################

class Score():

    def __init__(self) -> None:
        self.__score = 0
        self.__score_to_add = 10

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value

    # Monitors if points has been already added for wall passed player.
    # Adds points to score when wall is passed player.

    def add_points(self, walls : list):
        wall1 = walls[0][0]
        if wall1.change_is_points_added != True:

            if wall1.get_x < 100:
                wall1.change_is_points_added = True
                self.__score += self.__score_to_add

    # Function for printing the score
    def print_score(self, display):
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(f"Score: {self.__score}", True, (255, 0, 0))
        display.blit(text, (50, 50))
        
    # Function for taking care of both; adding points & printing the score
    def handle_score(self, walls, display):
        self.add_points(walls)
        self.print_score(display)

    