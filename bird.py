from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine


class Bird:
    def __init__(self, x=0, y=300):
        self.x, self.y = x, y
        self.target_x = 400
        self.speed = 100
        Bird.image = load_image('bird_animation.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        # 위치 업데이트 (목표 지점 400)
        if self.x < self.target_x:
            self.x += self.speed * game_framework.frame_time

        # 맵 끝 충돌 처리
        if self.x >= self.target_x:
            self.x = self.target_x
