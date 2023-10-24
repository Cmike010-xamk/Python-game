import pygame

#####################################################
############## Class for spacecraft #################

class Spacecraft():

    def __init__(self) -> None:
        self.__width = 40
        self.__height = 25
        self.__x = 100
        self.__y = 240
        self.__boost = False
        self.__spacecraft_image = pygame.image.load("Images/spacecraft.png")
        self.__move_down = True
        self.__move_up = False
        self.__hit_border = False
    
    # Moves spacecraft up and down
    def boostUp(self):
        if self.__boost:
            self.__y -= 4.5
            self.__move_down = False
            self.__move_up = True
        else:
            self.__y += 3.5
            self.__move_up = False
            self.__move_down = True
    
    def spacecraft_controls(self, e):
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.__boost = True
                
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                self.__boost = False

     # Keeps spacecraft vertically on screen
    def border_handler(self):
        if self.__y >= 455:
            self.__y = 455
            self.__hit_border = True

        elif self.__y <= 0:
            self.__y = 0
            self.__hit_border = True

        else:
            self.__hit_border = False

    # Check if hit with walls
    def wall_collision_checker(self, wall_container : list):
        wall1, wall2 = wall_container[0]
        if wall1.get_x >= self.__x and wall1.get_x <= self.__x + self.__width:
            if self.__y < wall1.get_height or self.__y + self.__height > wall2.get_y:
                return True
    
    def draw_spacecraft(self,display):
        # Handle sprite rotation based where spacecraft is going (up or down)
        if self.__hit_border:
            display.blit(self.__spacecraft_image, (self.__x, self.__y))
        else: 
            if self.__move_down:
                display.blit(pygame.transform.rotate(self.__spacecraft_image, -30), (self.__x, self.__y))
            if self.__move_up:
                display.blit(pygame.transform.rotate(self.__spacecraft_image, 30), (self.__x, self.__y))
                

    def handle_player(self, display):
        self.border_handler()
        self.boostUp()
        

        self.draw_spacecraft(display)
        
