import pygame
import spacecraft
import walls
import score


########################################################################
####################        Game class        ##########################

class Game():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Spacecraft")
        self.__clock = pygame.time.Clock()
        self.__player = spacecraft.Spacecraft()
        self.__wall_controller = walls.WallController()
        self.__player_score = score.Score()

        self.__display = pygame.display.set_mode((640, 480))

        self.__is_first_game_played = False
        self.__game_running = False

        self.game()

###################### Loop for playing the game ######################
#
# While true, we're listening events. All other events except quitting the game are passed to key-handler.
# Also listening if game has been started or not and calling game functions accordingly.

    def game(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                else: 
                    self.key_handler(e)

            if self.__is_first_game_played != True:
                font = pygame.font.SysFont("Arial", 24)
                text = font.render("Press SPACE to start", True, (255, 0, 0))
                self.__display.blit(text, (240, 200))
                pygame.display.flip()

            if self.__game_running:
                self.play_game()

            if self.__game_running != True and self.__is_first_game_played:
                self.game_over()
                
 ######################### Key handler ###########################
 # 
 #    
    def key_handler(self, e):

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if self.__is_first_game_played != True:
                        self.__is_first_game_played = True
                        self.__game_running = True

                if self.__is_first_game_played and self.__game_running != True:
                        self.__game_running = True

######################### Main game-function #####################
# Creates instaces of player and wall-controller if not exist. 
# Calls functions needed for playing the game.

    def play_game(self):

        if self.__player == None:
            self.__player = spacecraft.Spacecraft()
        if self.__wall_controller == None:
            self.__wall_controller = walls.WallController()

        # Reset score in beginning of game
        self.__player_score.score = 0
        
        # Events other than quit are passed to spacecraft_controls
        while self.__game_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                else:
                    self.__player.spacecraft_controls(e)

            self.__display.fill((0,0,0))

            # Control walls, score and player
            self.__wall_controller.handle_wall_controller(self.__display)
            self.__player_score.handle_score(self.__wall_controller.wall_container, self.__display)
            self.__player.handle_player(self.__display)

            # Set __game_running state if player collides with walls. Remove player & wall_controller, reset wall-speed.
            if self.__player.wall_collision_checker(self.__wall_controller.wall_container):
                self.__game_running = False
                self.__player = None
                self.__wall_controller = None
                walls.Wall.speed = 4

            # Make game more challengeable
            self.make_game_more_difficult(self.__player_score.score)
            pygame.display.flip()
            self.__clock.tick(60)

########################## Gamer over ############################
# 
    def game_over(self):
        font = pygame.font.SysFont("Arial", 24)
        text1 = font.render("GAME OVER ", True, (255, 0, 0))
        text2 = font.render(f"Score: {self.__player_score.score}", True, (255, 0 ,0))
        text3 = font.render("Press SPACE to play again", True, (255, 0, 0))
        self.__display.blit(text1, (240, 180))
        self.__display.blit(text2, (240, 210))
        self.__display.blit(text3, (240, 240))
        pygame.display.flip()

########################## Make game harder ######################
#
    def make_game_more_difficult(self, score):
        if score > 10:
            if score % 50 == 0:
                walls.Wall.speed += 0.001
                #print(walls.Wall.speed)

Game()
