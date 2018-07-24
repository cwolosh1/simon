import pygame
import random
import tile

class Controller:
    def __init__(self):
        # Initializes Pygame, the sound mixer, and sets the window caption.
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Simon")

        # Creates a DEBUG variable
        self.DEBUG = True

        # Instantiates objects and variables used for backend counting.
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.gametime = 0
        self.time_stamp = 0
        self.countdown = 0

        # Instantiates the game window and sets the background color.
        self.WIDTH = 750
        self.HEIGHT = 800
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.window.fill((40, 40, 40))

        # Instantiates all font types used in the UI.
        self.title = pygame.font.SysFont("Verdana", 72, bold=True)
        self.text = pygame.font.SysFont("Verdana", 24, italic=True)
        self.debug_font = pygame.font.SysFont("Verdana", 12)

        # Instantiates the four tile objects in the game, and the highlighter texture.
        self.highlighter = pygame.image.load("art/highlighter.png")
        self.red = tile.Tile("red")
        self.green = tile.Tile("green")
        self.yellow = tile.Tile("yellow")
        self.blue = tile.Tile("blue")

        # Creates variables to organize the different phases of gameplay.
        self.main_menu = True
        self.memory_phase_1 = False
        self.memory_phase_2 = False
        self.selection_phase = False

        # Sets a score variable to track the player's score, and sets an array that will determine the colors.
        self.score = 0
        self.remember_this = []

        the_game_is_running = True

        while the_game_is_running:
            for event in pygame.event.get():

                # Checks to see if the player clicks the 'X' at the top left of the window.
                if event.type == pygame.QUIT:
                    the_game_is_running = False

                # Check to see if the player clicks the mouse anywhere in the window.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu == True:
                        self.memory_phase_1 = True
                        self.main_menu = False

                # Checks to see if the player presses the 'd' key to toggle DEBUG mode.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and self.DEBUG == False:
                        self.DEBUG = True
                        print("DEBUG mode activated")
                    elif event.key == pygame.K_d and self.DEBUG == True:
                        self.DEBUG = False
                        print("DEBUG mode de-activated")

            self.window.fill((40, 40, 40))
            self.drawSquares()

            if self.main_menu:
                self.window.blit(self.title.render("Let's Play Simon!", True, (255,255,255)), (28,0))
                self.window.blit(self.text.render("Click Anywhere to Continue", True, (255,255,255)), (210,408))

            else:
                self.window.blit(self.text.render("Current Score: " + str(self.score), True, (255,255,255)), (500,30))

                if self.memory_phase_1:
                    self.beep_counter = 0
                    self.generateLevel()
                    self.memory_phase_1 = False
                    self.memory_phase_2 = True

                if self.memory_phase_2 and self.wait(1):
                    if self.beep_counter <= self.score:
                        self.rememberThis()
                        self.beep_counter += 1
                    else:
                        self.memory_phase_2 = False
                        self.selection_phase = True

                if self.selection_phase:
                    #self.playerInput()
                    #self.drawSquares()
                    self.score += 1
                    self.memory_phase_1 = True
                    self.selection_phase = False

            self.update()

        pygame.quit()

###############################################################################
# # # # # # # # Below are all of the methods for the controller # # # # # # # #
###############################################################################

    def drawSquares(self):
        self.window.blit(self.red.image, self.red.coords)
        self.window.blit(self.green.image, self.green.coords)
        self.window.blit(self.yellow.image, self.yellow.coords)
        self.window.blit(self.blue.image, self.blue.coords)

    def generateLevel(self):
        self.remember_this.append(random.randrange(4))

    def playerInput(self):
        for i in range(self.score + 1):
            the_player_has_not_clicked = True

            while the_player_has_not_clicked:
                the_player_has_not_clicked = False

    def rememberThis(self):
        i = self.remember_this[self.beep_counter]
        if i == 0:
            self.selectRed()
        elif i == 1:
            self.selectGreen()
        elif i == 2:
            self.selectYellow()
        elif i == 3:
            self.selectBlue()

    def selectRed(self):
        self.red.sound.play()
        self.red.selected = True
        self.window.blit(self.highlighter, self.red.coords)

    def selectGreen(self):
        self.green.sound.play()
        self.green.selected = True
        self.window.blit(self.highlighter, self.green.coords)

    def selectYellow(self):
        self.yellow.sound.play()
        self.yellow.selected = True
        self.window.blit(self.highlighter, self.yellow.coords)

    def selectBlue(self):
        self.blue.sound.play()
        self.blue.selected = True
        self.window.blit(self.highlighter, self.blue.coords)

    def update(self):

        self.counter += 1
        self.counter %= 60

        if self.counter == 0:
            self.gametime += 1

        if self.DEBUG:
            # Indicates if DEBUG mode has been activated. Serves as the header for the list of values.
            self.window.blit(self.debug_font.render("DEBUG mode has been activated:", True, (255,255,255)), (5,100))

            # Indicates which phase of gameplay is currently happening.
            if self.main_menu:
                self.window.blit(self.debug_font.render("Current Game Phase: Main Menu", True, (255,255,255)), (5,124))
            elif self.memory_phase_1 or self.memory_phase_2:
                self.window.blit(self.debug_font.render("Current Game Phase: Memory Phase", True, (255,255,255)), (5,124))
            elif self.selection_phase:
                self.window.blit(self.debug_font.render("Current Game Phase: Selection Phase", True, (255,255,255)), (5,124))

            # Displays the array of random integers that determine the color pattern.
            try:
                self.window.blit(self.debug_font.render("Randomly Generated List: " + str(self.remember_this), True, (255,255,255)), (5,136))
            except:
                self.window.blit(self.debug_font.render("Randomly Generated List: ", True, (255,255,255)), (5,136))

            # Displays total in game time in seconds.
            self.window.blit(self.debug_font.render("In Game Time (Seconds): " + str(self.gametime), True, (255,255,255)), (5,148))

        self.clock.tick(60)
        pygame.display.update()

    def wait(self, seconds):
        self.countdown = self.time_stamp - self.gametime + seconds

        if self.time_stamp == 0:
            self.time_stamp = self.gametime
        if self.gametime == self.time_stamp + seconds:
            self.time_stamp = 0
            return True
        else:
            return False





def main():
    Controller()
main()
