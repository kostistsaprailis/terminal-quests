import random
import numpy as np
from settings import settings
from termcolor import colored, cprint

class World(object):

    def __init__(self):

        self.size = settings['size']
        self.window = settings['window']
        self.map_l0 = np.zeros((settings['size'],settings['size']))
        self.map_l1 = np.zeros((settings['size'],settings['size']))
        self.p_map = ''
        self._generate_trees()
        self._generate_grass()

    def _generate_trees(self):
        for i in range(self.size * 5):
            treeX, treeY = int(np.random.rand() * self.size), int(np.random.rand() * self.size)
            self.map_l1[treeX, treeY] = 1.0

    def _generate_grass(self):
        for i in range(self.size * 5):
            treeX, treeY = int(np.random.rand() * self.size), int(np.random.rand() * self.size)
            self.map_l1[treeX, treeY] = 3.0

    def add_hero(self, hero):
        self.hero = hero
        self.map_l1[hero.posX, hero.posY] = 2.0

    def update_world(self):
        self.hero.update_hero()
        self.map_l1[self.hero.oldX, self.hero.oldY] = 0.0
        self.map_l1[self.hero.posX, self.hero.posY] = 2.0
        self.print_map()

    def print_map(self):
        if self.hero.posX > (settings['window'] / 2):
            startX = self.hero.posX - settings['window'] // 2
        else:
            startX = 0
        if self.hero.posY > (settings['window'] / 2):
            startY = self.hero.posY - settings['window'] // 2
        else:
            startY = 0
        print('\033[1;1H')
        for i in range(self.window):
            for j in range(self.window):
                if self.map_l1[startX + i, startY + j] == 1.0:
                    # self.p_map += u"\U0001F332"
                    cprint("\U0001F332", 'green', end='')
                elif self.map_l1[startX + i, startY + j] == 2.0:
                    self.p_map += "⛹"
                    cprint('⛹', end='')
                elif self.map_l1[startX + i, startY + j] == 3.0:
                    # self.p_map += u"\u4E35"
                    cprint("\u4E35", 'magenta', end='')
                elif self.map_l0[startX + i, startY + j] == 0.0:
                    # self.p_map += '.'
                    cprint(".", 'green', end='')
            # cprint(self.p_map, 'green')
            cprint('')
            self.p_map = ''
        print('(',startX,',',startY,')')
        print('Hero cur:', self.hero.posX, self.hero.posY)
        print('Hero prev:', self.hero.oldX, self.hero.oldY)
