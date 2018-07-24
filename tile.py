import pygame

class Tile:
    def __init__(self, color):

        if color == "red":
            self.image = pygame.image.load("art/red.png")
            self.sound = pygame.mixer.Sound("art/red_sound.ogg")
            self.coords = (400, 100)
        elif color == "green":
            self.image = pygame.image.load("art/green.png")
            self.sound = pygame.mixer.Sound("art/green_sound.ogg")
            self.coords = (50, 100)
        elif color == "yellow":
            self.image = pygame.image.load("art/yellow.png")
            self.sound = pygame.mixer.Sound("art/yellow_sound.ogg")
            self.coords = (50, 450)
        elif color == "blue":
            self.image = pygame.image.load("art/blue.png")
            self.sound = pygame.mixer.Sound("art/blue_sound.ogg")
            self.coords = (400, 450)
