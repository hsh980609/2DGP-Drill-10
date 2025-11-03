from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine

class Fly:
    def __init__(self, bird):
        self.bird = bird
        pass
    def enter(self, e):
        pass
    def exit(self, e):
        pass
    def do(self):
        pass
    def draw(self):
        if self.bird.face_dir == 1: # right
            self.bird.image.clip_draw(int(self.bird.frame) * 100, 100, 100, 100, self.bird.x, self.bird.y)
        else: # face_dir == -1: # left
            self.bird.image.clip_composite_draw(int(self.bird.frame) * 100, 0, 100, 100, 0,'h' , self.bird.x, self.bird.y)
        pass



class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()