from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine

class Fly:
    def __init__(self, bird):
        pass
    def enter(self, e):
        pass
    def exit(self, e):
        pass
    def do(self):
        pass
    def draw(self):
        pass



class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()