"""
Circle Dodge (Pygame)

A dodge-the-hazards mini-game where you play as a circle moving across a
QWERTY keyboard grid by pressing keys Q-P, A-L, and Z-M. Survive escalating
vertical, horizontal, key-tile, and circular attacks across increasing
difficulties until the timer finishes without losing all 3 lives.
"""

import random
import sys
import pygame
from pygame.locals import QUIT

pygame.init()

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Hello World!")
clock = pygame.time.Clock()

x = 450
y = 300
frame = 0
vertical_attack = False
horizontal_attack = False
key_attack = False
circle_attack = False
Difficulty = 0
attack_timer = 1000
key_coords = []

animation_vertical = 0
vertical_yes = False
colour_change_vertical = 0
deadtimer_vertical = 0
continuous_v = False

animation_horizontal = 0
horizontal_yes = False
colour_change_horizontal = 0
deadtimer_horizontal = 0
continuous_h = False

animation_key = 0
key_yes = False
colour_change_key = 0
deadtimer_key = 0
continuous_k = False

animation_circle = 0
circle_yes = False
colour_change_circle = 0
deadtimer_circle = 0
continuous_c = False
xd_c = 5

KEY_COORDS = {
    pygame.K_q: (135, 200), pygame.K_w: (205, 200), pygame.K_e: (275, 200),
    pygame.K_r: (345, 200), pygame.K_t: (415, 200), pygame.K_y: (485, 200),
    pygame.K_u: (555, 200), pygame.K_i: (625, 200), pygame.K_o: (695, 200),
    pygame.K_p: (765, 200),

    pygame.K_a: (170, 300), pygame.K_s: (240, 300), pygame.K_d: (310, 300),
    pygame.K_f: (380, 300), pygame.K_g: (450, 300), pygame.K_h: (520, 300),
    pygame.K_j: (590, 300), pygame.K_k: (660, 300), pygame.K_l: (730, 300),

    pygame.K_z: (205, 400), pygame.K_x: (275, 400), pygame.K_c: (345, 400),
    pygame.K_v: (415, 400), pygame.K_b: (485, 400), pygame.K_n: (555, 400),
    pygame.K_m: (625, 400),
}

keyboardlayout = [
    [135, 200], [205, 200], [275, 200], [345, 200], [415, 200],
    [485, 200], [555, 200], [625, 200], [695, 200], [765, 200],
    [170, 300], [240, 300], [310, 300], [380, 300], [450, 300],
    [520, 300], [590, 300], [660, 300], [730, 300],
    [205, 400], [275, 400], [345, 400], [415, 400], [485, 400],
    [555, 400], [625, 400],
]

deadzone = []
lives = 3
immunity_timer = 0
circle_coords_saver = []
running = True

print("Hello fellow circle! Dodge the red things until the time runs out! Type on the keyboard to move your character.")
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((0, 0, 0))

    for i in range(len(keyboardlayout)):
        x_axis = keyboardlayout[i][0]
        y_axis = keyboardlayout[i][1]
        pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(x_axis - 30, y_axis - 30, 60, 60), 2)

    keys = pygame.key.get_pressed()
    for key, (kx, ky) in KEY_COORDS.items():
        if keys[key]:
            x, y = kx, ky
            break

    if (x, y) in deadzone and immunity_timer == 0:
        lives = lives - 1
        print("ouch!", lives, "lives left!")
        immunity_timer = 2000

    if frame % random.randint(1, 100) == 0 and Difficulty == 0 and attack_timer == 0:
        random_attack = random.randint(1, 5)
        if random_attack == 5 or random_attack == 4:
            horizontal_attack = True
        else:
            vertical_attack = True
        attack_timer = 5000
    elif frame % random.randint(1, 70) == 0 and Difficulty == 1 and attack_timer == 0:
        random_attack = random.randint(1, 5)
        if random_attack == 1:
            vertical_attack = True
            key_attack = True
        elif random_attack == 2 or random_attack == 3:
            horizontal_attack = True
        else:
            key_attack = True
        attack_timer = 4000
    elif frame % random.randint(1, 50) == 0 and Difficulty == 2 and attack_timer == 0:
        random_attack = random.randint(1, 5)
        if random_attack == 1:
            vertical_attack = True
            horizontal_attack = True
        elif random_attack == 2:
            vertical_attack = True
            key_attack = True
        elif random_attack == 3:
            horizontal_attack = True
            circle_attack = True
        else:
            vertical_attack = True
            key_attack = True
            circle_attack = True
        attack_timer = 3000

    if vertical_attack:
        if Difficulty == 0:
            xd_v = 10
        elif Difficulty == 1:
            xd_v = 7
        else:
            xd_v = 5
        if not vertical_yes:
            randomizer_vertical = random.randint(0, 9)

        vertical_x = randomizer_vertical * 70 + 105

        if deadtimer_vertical == 0:
            pygame.draw.rect(
                DISPLAYSURF,
                (225 - colour_change_vertical, 225 - colour_change_vertical, 225 - colour_change_vertical),
                pygame.Rect(vertical_x, 30, 60, 60),
                2,
            )
            animation_vertical = animation_vertical + 1
            colour_change_vertical = animation_vertical // xd_v
            if colour_change_vertical > 225:
                colour_change_vertical = 225
            vertical_yes = True

        if colour_change_vertical == 225:
            pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(vertical_x, 0, 60, 600))
            deadzone.append((vertical_x + 30, 200))
            deadzone.append((vertical_x + 30, 400))
            deadzone.append((vertical_x - 5, 300))
            deadzone.append((vertical_x + 65, 300))
            continuous_v = True
            deadtimer_vertical = 100 * xd_v
            vertical_attack = False
            animation_vertical = 0
            colour_change_vertical = 0

    if horizontal_attack:
        if Difficulty == 0:
            xd_h = 10
        elif Difficulty == 1:
            xd_h = 7
        else:
            xd_h = 5
        if not horizontal_yes:
            randomizer_horizontal = random.randint(2, 4)
            if random.randint(0, 1) == 1:
                supriseattack = 850
            else:
                supriseattack = -15
        horizontal_y = randomizer_horizontal * 100 - 30

        if deadtimer_horizontal == 0:
            colour_change_horizontal = animation_horizontal // xd_h
            if colour_change_horizontal > 225:
                colour_change_horizontal = 225
            pygame.draw.rect(
                DISPLAYSURF,
                (225 - colour_change_horizontal, 225 - colour_change_horizontal, 225 - colour_change_horizontal),
                pygame.Rect(supriseattack, horizontal_y, 60, 60),
                2,
            )
            animation_horizontal = animation_horizontal + 1

            horizontal_yes = True

        if colour_change_horizontal == 225:
            pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(0, horizontal_y, 900, 60))
            continuous_h = True
            horizontal_attack = False
            animation_horizontal = 0
            colour_change_horizontal = 0
            deadtimer_horizontal = 100 * xd_h
            if horizontal_y == 170 or horizontal_y == 370:
                for i in range(9):
                    deadzone.append((i * 70 + 135, horizontal_y + 30))
            elif horizontal_y == 270:
                for i in range(8):
                    deadzone.append((i * 70 + 170, horizontal_y + 30))

    if key_attack:
        if Difficulty == 1:
            xd_k = 7
        elif Difficulty == 2:
            xd_k = 3
        if not key_yes:
            if Difficulty == 1:
                for i in range(3):
                    randomizer_key = random.randint(0, 25)
                    key_coords.append(randomizer_key)
            elif Difficulty == 2:
                for i in range(5):
                    randomizer_key = random.randint(0, 25)
                    key_coords.append(randomizer_key)
        if deadtimer_key == 0:
            for i in key_coords:
                pygame.draw.rect(
                    DISPLAYSURF,
                    (225 - colour_change_key, 225 - colour_change_key, 225 - colour_change_key),
                    pygame.Rect(keyboardlayout[i][0] - 30, keyboardlayout[i][1] - 30, 50, 50),
                )
            animation_key = animation_key + 1
            colour_change_key = animation_key // xd_k
            if colour_change_key > 225:
                colour_change_key = 225
            key_yes = True
        if colour_change_key == 225:
            for i in key_coords:
                pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(keyboardlayout[i][0] - 30, keyboardlayout[i][1] - 30, 60, 60))
            continuous_k = True
            key_attack = False
            animation_key = 0
            colour_change_key = 0
            deadtimer_key = 100 * xd_k
            for i in key_coords:
                deadzone.append((keyboardlayout[i][0], keyboardlayout[i][1]))

    if circle_attack:
        if not circle_yes:
            randomizer_circle = random.randint(0, 5)
            if randomizer_circle == 0:
                circle_coords_x = 200
                circle_coords_y = 250
            elif randomizer_circle == 1:
                circle_coords_x = 400
                circle_coords_y = 250
            elif randomizer_circle == 2:
                circle_coords_x = 600
                circle_coords_y = 250
            elif randomizer_circle == 3:
                circle_coords_x = 800
                circle_coords_y = 250
            elif randomizer_circle == 4:
                circle_coords_x = 300
                circle_coords_y = 350
            elif randomizer_circle == 5:
                circle_coords_x = 500
                circle_coords_y = 350
        if deadtimer_circle == 0:
            pygame.draw.circle(
                DISPLAYSURF,
                (225 - colour_change_circle, 225 - colour_change_circle, 225 - colour_change_circle),
                (circle_coords_x, circle_coords_y),
                100,
                2,
            )
            animation_circle = animation_circle + 1
            colour_change_circle = animation_circle // xd_c
            if colour_change_circle > 225:
                colour_change_circle = 225
            circle_yes = True
            if colour_change_circle == 225:
                pygame.draw.circle(DISPLAYSURF, (225, 0, 0), (circle_coords_x, circle_coords_y), 100)
                continuous_c = True
                circle_attack = False
                animation_circle = 0
                colour_change_circle = 0
                deadtimer_circle = 100 * xd_c
                for i in keyboardlayout:
                    if (
                        i[0] < 100 + circle_coords_x
                        and i[0] > circle_coords_x - 100
                        and i[1] < 100 + circle_coords_y
                        and i[1] > circle_coords_y - 100
                    ):
                        deadzone.append((i[0], i[1]))
                        circle_coords_saver.append((i[0], i[1]))

    if continuous_h:
        pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(0, horizontal_y, 900, 60))
        if deadtimer_horizontal == 1:
            deadtimer_horizontal = 0
            horizontal_yes = False
            continuous_h = False
            if horizontal_y == 170 or horizontal_y == 370:
                for i in range(9):
                    if (i * 70 + 135, horizontal_y + 30) in deadzone:
                        deadzone.remove((i * 70 + 135, horizontal_y + 30))
            elif horizontal_y == 270:
                for i in range(8):
                    if (i * 70 + 170, horizontal_y + 30) in deadzone:
                        deadzone.remove((i * 70 + 170, horizontal_y + 30))

    if continuous_v:
        pygame.draw.rect(DISPLAYSURF, (225, 0, 0), pygame.Rect(vertical_x, 0, 60, 600))
        if deadtimer_vertical == 1:
            deadtimer_vertical = 0
            vertical_yes = False
            continuous_v = False
            if (vertical_x + 30, 200) in deadzone:
                deadzone.remove((vertical_x + 30, 200))
            if (vertical_x + 30, 400) in deadzone:
                deadzone.remove((vertical_x + 30, 400))
            if (vertical_x - 5, 300) in deadzone:
                deadzone.remove((vertical_x - 5, 300))
            if (vertical_x + 65, 300) in deadzone:
                deadzone.remove((vertical_x + 65, 300))

    if continuous_k:
        for i in key_coords:
            pygame.draw.rect(
                DISPLAYSURF,
                (225, 0, 0),
                pygame.Rect(keyboardlayout[i][0] - 30, keyboardlayout[i][1] - 30, 60, 60),
            )
        if deadtimer_key == 1:
            deadtimer_key = 0
            key_yes = False
            continuous_k = False
            for i in key_coords:
                deadzone.remove((keyboardlayout[i][0], keyboardlayout[i][1]))
            key_coords.clear()

    if continuous_c:
        pygame.draw.circle(DISPLAYSURF, (225, 0, 0), (circle_coords_x, circle_coords_y), 100)
        if deadtimer_circle == 1:
            deadtimer_circle = 0
            circle_yes = False
            continuous_c = False
            for i in circle_coords_saver:
                if i in deadzone:
                    deadzone.remove((i[0], i[1]))

    # Draw the player last so it stays visible over hazards and clear frame redraws
    pygame.draw.circle(DISPLAYSURF, (225, 225, 225), (x, y), 10)

    pygame.display.flip()
    clock.tick(60)
    frame = frame + 1
    if immunity_timer > 0:
        immunity_timer = immunity_timer - 1
    if attack_timer > 0:
        attack_timer = attack_timer - 1
    if deadtimer_vertical > 0:
        deadtimer_vertical = deadtimer_vertical - 1
    if deadtimer_horizontal > 0:
        deadtimer_horizontal = deadtimer_horizontal - 1
    if deadtimer_key > 0:
        deadtimer_key = deadtimer_key - 1
    if deadtimer_circle > 0:
        deadtimer_circle = deadtimer_circle - 1
    if frame == 20000:
        Difficulty = 1
        print("difficulty up! 1/2")
    if frame == 50000:
        Difficulty = 2
        print("difficulty up! 2/2")
    if frame == 100000:
        print("YOU WIN! :)")
        pygame.quit()
        sys.exit()
    if lives <= 0:
        print("YOU LOSE :(")
        pygame.quit()
        sys.exit()


