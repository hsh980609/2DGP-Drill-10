from pico2d import *
import game_world
import game_framework
from state_machine import StateMachine


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_SPEED_KMPH = 30.0  # 시속 30km
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Bird:
    def __init__(self, x =0 , y=300):
        self.x, self.y = x, y
        self.speed = BIRD_SPEED_PPS
        self.face_dir = 1
        self.frame = 0
        Bird.image = load_image('bird_animation.png')

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 182, 0, 180, 170, 0, '', self.x, self.y, 100, 100)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 182, 0, 180, 170, 0, 'h', self.x, self.y, 100, 100)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * self.face_dir * game_framework.frame_time

        # 위치 업데이트
        if self.x >= 1600:
            self.x = 1600
            self.face_dir = -1

        elif self.x <= 0:
            self.x = 0
            self.face_dir = 1
