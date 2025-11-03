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
FRAMES_PER_ACTION = 14

CLIP_WIDTH = 180
CLIP_HEIGHT = 170

class Bird:
    def __init__(self, x =0 , y=300):
        self.x, self.y = x, y
        self.speed = BIRD_SPEED_PPS
        self.face_dir = 1
        self.frame = 0
        Bird.image = load_image('bird_animation.png')

    def draw(self):
        col = int(self.frame % 5)  # 열(0~4)
        row = int(self.frame // 5)  # 행(0~2)

        clip_x = col * CLIP_WIDTH
        clip_y = (2 - row) * CLIP_HEIGHT
        flip_value = ''

        if self.face_dir == -1:
            flip_value = 'h'

        self.image.clip_composite_draw(clip_x, clip_y, CLIP_WIDTH, CLIP_HEIGHT,0, flip_value, self.x, self.y, 100, 100)

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
