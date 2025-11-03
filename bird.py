from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine


class Bird:
    def __init__(self, x=400, y=300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        # 위치 업데이트

        # 맵 끝 충돌처리
        if self.x < 400:
            pass
        elif self.x < 0:
            pass
