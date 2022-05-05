import pygame
import random

WIDTH = 1000
HEIGHT = 600


def initialize():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Le Chats Demonstration")
    return window


def display_background(reaction, window):
    pygame.draw.rect(window, reaction.current_color, (0, 0, WIDTH, HEIGHT))


def display_reaction(reaction, window):
    font = pygame.font.SysFont("euphemia", 55, True)
    if "Cu(H2O)6(2+)" in reaction.reactants:
        font = pygame.font.SysFont("euphemia", 50, True)
    string = ""
    for reactant in reaction.reactants:
        string += reactant + " + "
    string = string[:-3]
    string += " <-> "
    for product in reaction.products:
        string += product + " + "
    string = string[:-2]
    text = font.render(string, True, (0, 0, 0))
    window.blit(text, (0, 0))


def buttons_BTB(window):
    for i in range(4):
        pygame.draw.rect(window, (0, 0, 0), (250 * i + 5, 510, 240, 80))
    font = pygame.font.SysFont("euphemia", 30, True)
    text = font.render("Add Heat                Remove Heat            Decrease [H+]            Increase [H+]", True, (255, 255, 255))
    window.blit(text, (70, 520))
    text = font.render("Add NaOH                  Add HCl", True, (100, 100, 100))
    window.blit(text, (570, 560))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 245:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 240, 80), 5)
            if pressed:
                return 1
        elif 255 <= mouse[0] <= 495:
            pygame.draw.rect(window, (255, 255, 255), (255, 510, 240, 80), 5)
            if pressed:
                return 2
        elif 505 <= mouse[0] <= 745:
            pygame.draw.rect(window, (255, 255, 255), (505, 510, 240, 80), 5)
            if pressed:
                return 3
        elif 755 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (755, 510, 240, 80), 5)
            if pressed:
                return 4
    return 0

def buttons_cobalt(window):
    for i in range(5):
        pygame.draw.rect(window, (0, 0, 0), (200 * i + 5, 510, 190, 80))
    font = pygame.font.SysFont("euphemia", 30, True)
    text = font.render("Add Heat         Remove Heat      Increase [Cl-]        Decrease            Increase", True, (255, 255, 255))
    window.blit(text, (50, 515))
    text = font.render("[Cl-] & [Co4+]          Volume", True, (255, 255, 255))
    window.blit(text, (620, 535))
    text = font.render("Add NaCl            Add AgNo3        Add Water", True, (100, 100, 100))
    window.blit(text, (440, 560))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 195:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 190, 80), 5)
            if pressed:
                return 1
        elif 200 <= mouse[0] <= 395:
            pygame.draw.rect(window, (255, 255, 255), (205, 510, 190, 80), 5)
            if pressed:
                return 2
        elif 405 <= mouse[0] <= 595:
            pygame.draw.rect(window, (255, 255, 255), (405, 510, 190, 80), 5)
            if pressed:
                return 3
        elif 605 <= mouse[0] <= 795:
            pygame.draw.rect(window, (255, 255, 255), (605, 510, 190, 80), 5)
            if pressed:
                return 4
        elif 805 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (805, 510, 190, 80), 5)
            if pressed:
                return 5
    return 0

def buttons_iron(window):
    for i in range(4):
        pygame.draw.rect(window, (0, 0, 0), (250 * i + 5, 510, 240, 80))
    font = pygame.font.SysFont("euphemia", 29, True)
    text = font.render("Increase [K+]                   Increase [Fe+]                   Decrease                          Increase", True, (255, 255, 255))
    window.blit(text, (70, 520))
    text = font.render("[SCN-]                         [K+] & [SCN-]", True, (255, 255, 255))
    window.blit(text, (590, 540))
    text = font.render("Add KNO3                      Add FeCl3                     Add Na2HPO                     Add KSCN", True, (100, 100, 100))
    window.blit(text, (80, 565))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 245:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 240, 80), 5)
            if pressed:
                return 3
        elif 255 <= mouse[0] <= 495:
            pygame.draw.rect(window, (255, 255, 255), (255, 510, 240, 80), 5)
            if pressed:
                return 4
        elif 505 <= mouse[0] <= 745:
            pygame.draw.rect(window, (255, 255, 255), (505, 510, 240, 80), 5)
            if pressed:
                return 5
        elif 755 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (755, 510, 240, 80), 5)
            if pressed:
                return 6
    return 0

def buttons_sulphate(window):
    for i in range(5):
        pygame.draw.rect(window, (0, 0, 0), (250 * i + 5, 510, 240, 80))
    font = pygame.font.SysFont("euphemia", 35, True)
    text = font.render("Add Heat          Remove Heat         Increase [NH3]     Decrease [NH3]", True, (255, 255, 255))
    window.blit(text, (60, 520))
    text = font.render("Add NH3               Add HCl", True, (100, 100, 100))
    window.blit(text, (570, 560))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 245:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 240, 80), 5)
            if pressed:
                return 1
        elif 255 <= mouse[0] <= 495:
            pygame.draw.rect(window, (255, 255, 255), (255, 510, 240, 80), 5)
            if pressed:
                return 2
        elif 505 <= mouse[0] <= 745:
            pygame.draw.rect(window, (255, 255, 255), (505, 510, 240, 80), 5)
            if pressed:
                return 3
        elif 755 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (755, 510, 240, 80), 5)
            if pressed:
                return 4
    return 0

def buttons_copper(window):
    for i in range(5):
        pygame.draw.rect(window, (0, 0, 0), (500 * i + 5, 510, 490, 80))
    font = pygame.font.SysFont("euphemia", 35, True)
    text = font.render("Increase [H+] & [Cl-]                              Increase Volume", True, (255, 255, 255))
    window.blit(text, (120, 520))
    text = font.render("Add HCl                                          Add Water", True, (100, 100, 100))
    window.blit(text, (200, 560))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 495:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 490, 80), 5)
            if pressed:
                return 1
        elif 505 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (505, 510, 490, 80), 5)
            if pressed:
                return 2
    return 0

def buttons_methyl(window):
    for i in range(5):
        pygame.draw.rect(window, (0, 0, 0), (500 * i + 5, 510, 490, 80))
    font = pygame.font.SysFont("euphemia", 35, True)
    text = font.render("Increase Pressure                              Decrease Pressure", True, (255, 255, 255))
    window.blit(text, (120, 520))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 510 <= mouse[1] <= 590:
        if 5 <= mouse[0] <= 495:
            pygame.draw.rect(window, (255, 255, 255), (5, 510, 490, 80), 5)
            if pressed:
                return 1
        elif 505 <= mouse[0] <= 995:
            pygame.draw.rect(window, (255, 255, 255), (505, 510, 490, 80), 5)
            if pressed:
                return 2
    return 0

def choose_reaction(window):
    pygame.draw.rect(window, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
    for y in range(2):
        for x in range(3):
            pygame.draw.rect(window, (0, 0, 0), (333*x + 10, 100 + 200 * y, 313, 190))
            font = pygame.font.SysFont("euphemia", 150, True)
    text = font.render("BTB", True, (255, 255, 255))
    window.blit(text, (40, 150))
    font = pygame.font.SysFont("euphemia", 45, True)
    text = font.render("Iron (III) Chloride", True, (255, 255, 255))
    window.blit(text, (350, 150))
    text = font.render("Potassium", True, (255, 255, 255))
    window.blit(text, (400, 180))
    text = font.render("Thiocyanate", True, (255, 255, 255))
    window.blit(text, (390, 210))
    font = pygame.font.SysFont("euphemia", 39, True)
    text = font.render("Copper (II) Sulphate", True, (255, 255, 255))
    window.blit(text, (685, 160))
    text = font.render("Ammonia", True, (255, 255, 255))
    window.blit(text, (760, 190))
    text = font.render("Copper (II) Chloride", True, (255, 255, 255))
    window.blit(text, (20, 370))
    text = font.render("HCl", True, (255, 255, 255))
    window.blit(text, (140, 400))
    text = font.render("Cobalt (II) Chloride", True, (255, 255, 255,))
    window.blit(text, (360, 370))
    text = font.render("Hexahydrate", True, (255, 255, 255))
    window.blit(text, (410, 400))
    font = pygame.font.SysFont("euphemia", 70, True)
    text = font.render("Methyl Red", True, (255, 255, 255))
    window.blit(text, (680, 370))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 100 <= mouse[1] <= 290:
        if 10 <= mouse[0] <= 323:
            pygame.draw.rect(window, (0, 0, 255), (10, 100, 313, 190), 5)
            if pressed:
                return 1
        elif 343 <= mouse[0] <= 656:
            pygame.draw.rect(window, (0, 0, 255), (343, 100, 313, 190), 5)
            if pressed:
                return 2
        elif 676 <= mouse[0] <= 989:
            pygame.draw.rect(window, (0, 0, 255), (676, 100, 313, 190), 5)
            if pressed:
                return 3
    if 300 <= mouse[1] <= 490:
        if 10 <= mouse[0] <= 323:
            pygame.draw.rect(window, (0, 0, 255), (10, 300, 313, 190), 5)
            if pressed:
                return 4
        elif 343 <= mouse[0] <= 656:
            pygame.draw.rect(window, (0, 0, 255), (343, 300, 313, 190), 5)
            if pressed:
                return 5
        elif 676 <= mouse[0] <= 989:
            pygame.draw.rect(window, (0, 0, 255), (676, 300, 313, 190), 5)
            if pressed:
                return 6
    return False


def product_shift(window):
    font = pygame.font.SysFont("euphemia", 120, True)
    text = font.render("Product Shift!", True, (255, 255, 255))
    window.blit(text, (150, 200))
    pygame.display.update()
    pygame.time.wait(300)

def reactant_shift(window):
    font = pygame.font.SysFont("euphemia", 120, True)
    text = font.render("Reactant Shift!", True, (255, 255, 255))
    window.blit(text, (150, 200))
    pygame.display.update()
    pygame.time.wait(300)


def ppt(window):
    for i in range(100):
        pygame.draw.rect(window, (255, 255, 255), (random.randint(0, WIDTH), random.randint(400, 500), 5, 5))

def back_button(window):
    pygame.draw.rect(window, (0, 0, 0), (5, 40, 90, 40))
    font = pygame.font.SysFont("euphemia", 40, True)
    text = font.render("Back", True, (255, 255, 255))
    window.blit(text, (13, 47))
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    if 40 <= mouse[1] <= 80 and 5 <= mouse[0] <= 95:
        pygame.draw.rect(window, (255, 255, 255), (5, 40, 90, 40), 5)
        if pressed:
            return True
    return False