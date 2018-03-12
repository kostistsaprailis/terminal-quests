import os
import time
from world import World
from hero import Hero

def update_game_state(world):
    """ """
    world.update_world()
    time.sleep(0.1)

if __name__ == '__main__':
    os.system('clear')
    world = World()
    hero = Hero()
    world.add_hero(hero)

    while True:
        update_game_state(world)
