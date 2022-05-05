import pygame
class Reaction:
    def __init__(self, start_color, color_increment, reactants, products):
        # Start color: a list representing the unedited equilibrium
        self.current_color = pygame.Color(start_color)
        self.current_red = start_color[0]
        self.current_green = start_color[1]
        self.current_blue = start_color[2]
        # Color increment: a list representing the change in color WHEN A PRODUCT SHIFT OCCURS
        self.color_increment = color_increment
        # Reactants: a list of strings representing the reactants
        self.reactants = reactants
        # Products: a list of strings representing the products
        self.products = products

    def increment(self):
        self.current_red += self.color_increment[0]
        self.current_green += self.color_increment[1]
        self.current_blue += self.color_increment[2]
        if self.current_red < 0:
            self.current_red = 0
        if self.current_green < 0:
            self.current_green = 0
        if self.current_blue < 0:
            self.current_blue = 0
        if self.current_red > 255:
            self.current_red = 255
        if self.current_blue > 255:
            self.current_blue = 255
        if self.current_green > 255:
            self.current_green = 255
        self.current_color = pygame.Color(self.current_red, self.current_green, self.current_blue)

    def decrement(self):
        self.current_red -= self.color_increment[0]
        self.current_green -= self.color_increment[1]
        self.current_blue -= self.color_increment[2]
        if self.current_red < 0:
            self.current_red = 0
        if self.current_green < 0:
            self.current_green = 0
        if self.current_blue < 0:
            self.current_blue = 0
        if self.current_red > 255:
            self.current_red = 255
        if self.current_blue > 255:
            self.current_blue = 255
        if self.current_green > 255:
            self.current_green = 255
        self.current_color = pygame.Color(self.current_red, self.current_green, self.current_blue)
