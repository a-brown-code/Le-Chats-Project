import pygame
from reaction import Reaction
import Display

window = Display.initialize()

running = True
while running:
    react = False
    BTB = Reaction([67, 106, 44], [60, 11, -20], ["H+", "BTB-"], ["HBTB"])
    sulphate = Reaction([69, 118, 206], [8, 23, 4], ["CuSO4", "4NH3"], ["(Cu(NH3)4)SO4"])
    iron = Reaction([184, 15, 20], [-26, -38, -37], ["FeCl3", "3KSCN"], ["Fe(SCN)3", "3KCl"])
    methyl = Reaction([241, 74, 36], [20, 50, -25], ["H2O", "CO2", "2MR-"], ["2HMR", "CO3"])
    cobalt = Reaction([189, 4, 164], [-70, -55, -1], ["Co(H2O)6 (2+)", "4Cl-"], ["CoCl4 (2-)", "6H2O"])
    copper = Reaction([0, 206, 255], [70, -40, -255], ["Cu(H2O)6(2+)", "4HCl"], ["CuCl4(2-)", "6H2O", "4H+"])
    while running and not react:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        react = Display.choose_reaction(window)
        pygame.display.update()

    if react == 1:
        react = BTB
    elif react == 2:
        react = iron
    elif react == 3:
        react = sulphate
    elif react == 4:
        react = copper
    elif react == 5:
        react = cobalt
    else:
        react = methyl

    running = True
    count = 0
    while running:
        for event in pygame.event.get():

            # This ensures that the game can quit properly
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        Display.display_background(react, window)
        Display.display_reaction(react, window)
        back = Display.back_button(window)
        if back:
            break
        if react == BTB:
            pressed = Display.buttons_BTB(window)
            pygame.display.update()
            if (pressed == 2 or pressed == 3 or pressed == 5) and count > -3:
                BTB.decrement()
                count -= 1
                Display.reactant_shift(window)
            elif (pressed == 1 or pressed == 4) and count < 3:
                BTB.increment()
                count += 1
                Display.product_shift(window)
            continue
        elif react == sulphate:
            pressed = Display.buttons_sulphate(window)
            if count > 0:
                Display.ppt(window)
            pygame.display.update()
            if (pressed == 1 or pressed == 3) and count < 2:
                sulphate.increment()
                count += 1
                Display.product_shift(window)
            elif (pressed == 2 or pressed == 4) and count > -2:
                sulphate.decrement()
                count -= 1
                Display.reactant_shift(window)
            continue
        elif react == iron:
            pressed = Display.buttons_iron(window)
            pygame.display.update()
            if (pressed == 4 or pressed == 6) and count < 2:
                iron.increment()
                count += 1
                Display.product_shift(window)
            elif (pressed == 3 or pressed == 5) and count > -2:
                iron.decrement()
                count -= 1
                Display.reactant_shift(window)
            continue
        elif react == methyl:
            pressed = Display.buttons_methyl(window)
            pygame.display.update()
            if (pressed == 2) and count < 2:
                methyl.increment()
                count += 1
                Display.product_shift(window)
            elif (pressed == 1) and count > -2:
                methyl.decrement()
                count -= 1
                Display.reactant_shift(window)
            continue
        elif react == cobalt:
            pressed = Display.buttons_cobalt(window)
            pygame.display.update()
            if (pressed == 1 or pressed == 3) and count < 2:
                cobalt.increment()
                count += 1
                Display.product_shift(window)
            elif (pressed == 2 or pressed == 4 or pressed == 5) and count > -2:
                cobalt.decrement()
                count -= 1
                Display.reactant_shift(window)
            continue
        elif react == copper:
            pressed = Display.buttons_copper(window)
            pygame.display.update()
            if (pressed == 1) and count < 2:
                copper.increment()
                count += 1
                Display.product_shift(window)
            elif (pressed == 2) and count > -2:
                copper.decrement()
                count -= 1
                Display.reactant_shift(window)
            continue
