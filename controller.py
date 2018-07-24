import pygame
import random
import time
import tile

DEBUG = False

WIDTH = 750
HEIGHT = 800

class Controller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Simon")

        self.clock = pygame.time.Clock()
        self.counter = 0
        self.gametime = 1
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.window.fill((40, 40, 40))

        self.title = pygame.font.SysFont("Verdana", 72, bold=True)
        self.text = pygame.font.SysFont("Verdana", 24, italic=True)
        self.debug_font = pygame.font.SysFont("Verdana", 12)

        self.highlighter = pygame.image.load("art/highlighter.png")
        self.red = tile.Tile("red")
        self.green = tile.Tile("green")
        self.yellow = tile.Tile("yellow")
        self.blue = tile.Tile("blue")

        self.score = 0
        self.main_menu = True
        self.phase_1 = False
        self.phase_2 = False

        the_game_is_running = True

        while the_game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    the_game_is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.main_menu = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and DEBUG == False:
                        DEBUG == True
                    if event.key == pygame.K_d and DEBUG == True:
                        DEBUG == False

            if self.main_menu:
                self.window.blit(self.title.render("Let's Play Simon!", True, (255,255,255)), (28,0))
                self.window.blit(self.text.render("Click Anywhere to Continue", True, (255,255,255)), (210,408))

            else:
                if self.phase_1:
                    self.generateLevel()
                    self.rememberThis()

                if self.phase_2:
                    self.playerInput()
                    self.drawSquares()


            self.update()



        pygame.quit()

    def drawSquares(self):
        self.window.blit(self.red.image,  self.red.coords)
        self.window.blit(self.green.image,  self.green.coords)
        self.window.blit(self.yellow.image,  self.yellow.coords)
        self.window.blit(self.blue.image,  self.blue.coords)

    def generateLevel(self):
        self.remember_this = []
        for i in range(self.score + 1):
            self.remember_this.append(random.randrange(4))

    def playerInput(self):
        for i in range(self.score + 1):
            the_player_has_not_clicked = True

            while the_player_has_not_clicked:
                the_player_has_not_clicked = False

    def rememberThis(self):
        for i in self.remember_this:
            if i == 0:
                self.selectRedSquare()
            elif i == 1:
                self.selectGreenSquare()
            elif i == 2:
                self.selectYellowSquare()
            elif i == 3:
                self.selectBlueSquare()

    def selectRedSquare(self):
        self.red.sound.play()
        self.window.blit(self.highlighter, self.red.coords)

    def selectGreenSquare(self):
        self.green.sound.play()
        self.window.blit(self.highlighter, self.green.coords)

    def selectYellowSquare(self):
        self.yellow.sound.play()
        self.window.blit(self.highlighter, self.yellow.coords)

    def selectBlueSquare(self):
        self.blue.sound.play()
        self.window.blit(self.highlighter, self.blue.coords)

    def update(self):
        self.drawSquares()
        self.counter += 1
        self.counter %= 60
        pygame.display.update()
        self.clock.tick(60)

        if DEBUG and self.counter == 0:
            self.window.blit(self.debug_font.render("In Game Time (Seconds): " + str(self.gametime), True, (255,255,255)), (28,0))

            if self.main_menu:
                self.window.blit(self.debug_font.render("Current Game Phase: Main Menu" , True, (255,255,255)), (28,0))
            elif self.phase_1:
                self.window.blit(self.debug_font.render("Current Game Phase: Memory Phase", True, (255,255,255)), (28,0))
            elif self.phase_2:
                self.window.blit(self.debug_font.render("Current Game Phase: Selection Phase", True, (255,255,255)), (28,0))
            print("In Game Time (seconds): " + str(self.gametime))
            self.gametime += 1





def main():
    Controller()
main()
