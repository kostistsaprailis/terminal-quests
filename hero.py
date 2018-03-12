import random

from settings import settings

class Hero(object):

    def __init__(self):
        self.oldX = 0
        self.oldY = 0
        self.posX = random.randint(settings['window'], settings['size'] - settings['window'])
        self.posY = random.randint(settings['window'], settings['size'] - settings['window'])
        self.oldX = self.posX
        self.oldY = self.posY
        self.health = 32
        self.move = 0

    def update_hero(self):
        self.prev_move = self.move
        if random.randint(0,9) > 7:
            self.move = random.randint(0,3)
        if self.move == 0:
            if self.posX > 0:
                self.oldX = self.posX
                self.oldY = self.posY
                self.posX -= 1
        elif self.move == 1:
            if self.posY < settings['size']:
                self.oldY = self.posY
                self.oldX = self.posX
                self.posY += 1
        elif self.move == 2:
            if self.posX < settings['size']:
                self.oldX = self.posX
                self.oldY = self.posY
                self.posX += 1
        elif self.move == 3:
            if self.posY > 0:
                self.oldY = self.posY
                self.oldX = self.posX
                self.posY -= 1