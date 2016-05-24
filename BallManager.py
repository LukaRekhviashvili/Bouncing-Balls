import pygame
import MyRandom
from random import randint

class BallManager:
    balls = []

    def __init__(self, screen, rightBorder, leftBorder):
        self.screen = screen
        self.rightBorder = rightBorder
        self.leftBorder = leftBorder

    def addBall(self, ball):
        self.balls.append(ball)
        print "ball created on ", ball.position

    def drawBalls(self):
        for ball in self.balls:
            pygame.draw.circle(self.screen, ball.color, ball.position, ball.rad)

    def moveBalls(self):
        for ball in self.balls:
            ball.move()
            ball.checkPos(self.rightBorder, self.leftBorder)

        for i in range(0, len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball_1 = self.balls[i]
                ball_2 = self.balls[j]

                if self.hasCollision(ball_1, ball_2):
                    ball_1.velocity, ball_2.velocity = self.getNewVelocity(ball_1, ball_2)

                    ball_1.move()
                    ball_2.move()

                    ball_1.color = MyRandom.color()
                    ball_2.color = MyRandom.color()


    def hasCollision(self, ball_1, ball_2):
        cordDistanceSquare = (ball_1.position[0] - ball_2.position[0]) ** 2 + (ball_1.position[1] - ball_2.position[1]) ** 2
        radDistanceSquare = (ball_1.rad + ball_2.rad) ** 2

        if cordDistanceSquare < radDistanceSquare:
            return True

        return False

    def getCollisionPoint(self, ball_1, ball_2):
        collisionPointX = ((ball_1.position[0] * ball_2.rad)
                          + (ball_2.position[0] * ball_1.rad))\
                          / (ball_1.rad + ball_2.rad)

        collisionPointY = ((ball_1.position[1] * ball_2.rad)
                          + (ball_2.position[1] * ball_1.rad)) \
                          / (ball_1.rad + ball_2.rad)

        return [collisionPointX, collisionPointY]

    def getNewVelocity(self, ball_1, ball_2):
        newVelX1 = (ball_1.velocity[0] * (ball_1.mass - ball_2.mass) +
                    (2 * ball_2.mass * ball_2.velocity[0])) / (ball_1.mass + ball_2.mass);

        newVelY1 = (ball_1.velocity[1] * (ball_1.mass - ball_2.mass) +
                    (2 * ball_2.mass * ball_2.velocity[1])) / (ball_1.mass + ball_2.mass);

        newVelX2 = (ball_2.velocity[0] * (ball_2.mass - ball_1.mass) +
                    (2 * ball_1.mass * ball_1.velocity[0])) / (ball_1.mass + ball_2.mass);

        newVelY2 = (ball_2.velocity[1] * (ball_2.mass - ball_1.mass) +
                    (2 * ball_1.mass * ball_1.velocity[1])) / (ball_1.mass + ball_2.mass);

        return [newVelX1, newVelY1], [newVelX2, newVelY2]
