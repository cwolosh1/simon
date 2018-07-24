import pygame

class Tile:
    def __init__(self, color):
        if color == "red":
            self.color = color
            self.image = pygame.image.load("art/red.png")
            self.sound = pygame.mixer.Sound("art/red_sound.ogg")
            self.coords = (400, 100)
            self.selected = False

        elif color == "green":
            self.color = color
            self.image = pygame.image.load("art/green.png")
            self.sound = pygame.mixer.Sound("art/green_sound.ogg")
            self.coords = (50, 100)
            self.selected = False

        elif color == "yellow":
            self.color = color
            self.image = pygame.image.load("art/yellow.png")
            self.sound = pygame.mixer.Sound("art/yellow_sound.ogg")
            self.coords = (50, 450)
            self.selected = False
            
        elif color == "blue":
            self.color = color
            self.image = pygame.image.load("art/blue.png")
            self.sound = pygame.mixer.Sound("art/blue_sound.ogg")
            self.coords = (400, 450)
            self.selected = False
