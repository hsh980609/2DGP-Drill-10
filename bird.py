from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Bird:
    def __init__(self, x=0, y=300):
        self.x, self.y = x, y
        self.speed = 100
        self.face_dir = 1
        self.frame = 0
        Bird.image = load_image('bird_animation.png')

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 182, 0, 180, 160, 0, '', self.x, self.y, 100, 100)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * self.face_dir * game_framework.frame_time

        # 위치 업데이트
        if self.x >= 800:
            self.x = 800

        elif self.x <= 0:
            self.x = 0
            self.face_dir = 1
