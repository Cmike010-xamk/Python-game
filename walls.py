import pygame
import random

############################################################
########### Class for controlling walls ####################

class WallController():

    def __init__(self) -> None:
        self.wall_container = []
        self.__color_setter = [30,30,30]
        self.__color_value = 10
    # Add more walls
    def add_more_walls(self):
        while len(self.wall_container) < 2:
            self.generate_walls()

    # Adjust color-values to be given to wall-object as a parameter.
    def adjust_color(self):
        if self.__color_setter[0] != 240 and self.__color_setter[0] != 20:
            self.__color_setter[0] += self.__color_value
            return self.__color_setter
        if (self.__color_setter[0] == 240 or self.__color_setter[0] == 20) and (self.__color_setter[1] != 240 and self.__color_setter[1] != 20):
            self.__color_setter[1] += self.__color_value
            return self.__color_setter
        if (self.__color_setter[0] == 240 or self.__color_setter[0] == 20) and (self.__color_setter[1] == 240 or self.__color_setter[1] == 20) and (self.__color_setter[2] != 240 and self.__color_setter[2] != 20):
            self.__color_setter[2] += self.__color_value
            return self.__color_setter
        if self.__color_setter[0] == 240 and self.__color_setter[1] == 240 and self.__color_setter[2] == 240:
            self.__color_value = -10
            self.__color_setter[0] += self.__color_value
            self.__color_setter[1] += self.__color_value
            self.__color_setter[2] += self.__color_value 
            return self.__color_setter
        if self.__color_setter[0] == 20 and self.__color_setter[1] == 20 and self.__color_setter[2] == 20:
            self.__color_value = 10
            self.__color_setter[0] += self.__color_value
            self.__color_setter[1] += self.__color_value
            self.__color_setter[2] += self.__color_value
            return self.__color_setter
        
    # Generates pair of walls
    def generate_wall_pair(self):
        wall1 = Wall(random.randint(0,450), 0, self.adjust_color())
        wall2 = Wall(450-(wall1.get_height), 600-(400-(wall1.get_height)), self.__color_setter)
        return [wall1, wall2]
    
    # Adds wall pairs in to array
    def generate_walls(self):

        self.wall_container.append(self.generate_wall_pair())

    # Moves wall pairs and removes walls that are out of display
    def fly_walls(self, display):
        if len(self.wall_container) > 0:
            wall1, wall2 = self.wall_container[0]
            if wall1.get_x >= 200 and wall1.get_x < 650:
                wall1.move()
                wall2.move()
                wall1.draw_wall(display)
                wall2.draw_wall(display)

            if wall1.get_x > 0 and wall1.get_x < 200:
                wall3, wall4 = self.wall_container[1]
                wall1.move()
                wall2.move()
                wall3.move()
                wall4.move()
                wall1.draw_wall(display)
                wall2.draw_wall(display)
                wall3.draw_wall(display)
                wall4.draw_wall(display)

            if wall1.get_x <= 0:
                self.wall_container.pop(0)
    
        # Main function for controlling wall_controller
    def handle_wall_controller(self, display):
        self.add_more_walls()
        self.fly_walls(display)



#########################################################
############### Class for walls #########################

class Wall():

    speed = 4

    def __init__(self, height, y, color) -> None:
        self.__width = 10
        self.__height = height
        self.__x = 600
        self.__y = y
        self.__color = color
        self.__is_points_added = False

    def __str__(self) -> str:
        return f"{self}"
        
    def move(self):
        self.__x -= Wall.speed

    def draw_wall(self, display):
        pygame.draw.rect(display,(self.__color[0], self.__color[1], self.__color[2]), 
                         (self.__x, self.__y, self.__width, self.__height))

    @property
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x
    
    @property
    def get_y(self):
        return self.__y
    
    @property
    def change_is_points_added(self):
        return self.__is_points_added
    
    # Check if points that have passed player has added points to score only once
    @change_is_points_added.setter
    def change_is_points_added(self, value: bool):
        if self.__is_points_added != True:
            self.__is_points_added = value