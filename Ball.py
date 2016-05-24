import math

class Ball:
    def __init__(self, position, velocity, radius, color):
        self.position = position
        self.velocity = velocity
        self.rad = radius
        self.color = color
        self.mass = int(math.pi * (self.rad ** 2))

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def checkPos(self, rightBoundary, downBoundary):
        if self.position[0] + self.rad > rightBoundary :
            self.velocity[0] *= -1
            self.position[0] = rightBoundary - self.rad

        if self.position[0] - self.rad < 0:
            self.velocity[0] *= -1
            self.position[0] = self.rad

        if self.position[1] + self.rad > downBoundary :
            self.velocity[1] *= -1
            self.position[1] = downBoundary - self.rad

        if self.position[1] - self.rad < 0:
            self.velocity[1] *= -1
            self.position[1] = self.rad
