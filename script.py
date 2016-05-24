#!/usr/bin/python
import pygame
import MyRandom

from random import randint
from Ball import Ball
from BallManager import BallManager


def adjust_screen():
    pygame.init()

    videoinfo = pygame.display.Info()
    scr_width, scr_height = videoinfo.current_w, videoinfo.current_h

    scr_screen = pygame.display.set_mode((scr_width, scr_height))

    pygame.display.toggle_fullscreen()

    return scr_screen, scr_width, scr_height


def create_balls_radomly(ballmanager, amount):
    for i in range(0, amount):
        randomVelocity = [randint(-10, 10), randint(-10, 10)]
        randomRadius = randint(40, 50)
        randomPosition = [randint(60, width - 60), randint(60, height - 60)]
        fixedPosition = [100 + i * 100 % 1200, 100 + (i * 100) / 1200 * 100]

        ballmanager.addBall(Ball( fixedPosition, randomVelocity, randomRadius, MyRandom.color()))


# 2 - Initialize the game
screen, width, height = adjust_screen()

# BallManager instance
ballManager = BallManager(screen, width, height)

#ballManager.addBall(Ball([100, 100], [1, 4], 45, (255, 0, 0)))
#ballManager.addBall(Ball([500, 300], [-3, 2], 15, (0, 255, 0)))

# Adding Balls
create_balls_radomly(ballManager, 10)

# Main Loop
while 1:
    pygame.time.wait(20)

    # 5 - clear the screen before drawing it again
    screen.fill((255, 255, 255))

    # 6 - draw the screen elements
    ballManager.drawBalls()

    # 7 - update the screen
    pygame.display.flip()

    # movement
    ballManager.moveBalls()

    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                exit(0)
