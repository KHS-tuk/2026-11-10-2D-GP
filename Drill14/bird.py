from pico2d import load_image

import game_framework


class Bird:
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAME_COUNT = 14
    IMAGE_WIDTH = 918
    IMAGE_HEIGHT = 506
    DRAW_WIDTH = 110
    DRAW_HEIGHT = 100
    FRAMES_PER_SECOND = 12.0
    SPEED = 180.0

    image = None

    def __init__(self, x, y):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y
        self.frame = 0.0
        self.direction = 1

    def update(self):
        frame_time = game_framework.frame_time
        self.frame = (
            self.frame + self.FRAMES_PER_SECOND * frame_time
        ) % self.FRAME_COUNT
        self.x += self.direction * self.SPEED * frame_time

    def draw(self):
        frame_index = int(self.frame)
        column = frame_index % 5
        row = frame_index // 5
        source_y = self.IMAGE_HEIGHT - (row + 1) * self.FRAME_HEIGHT
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            column * self.FRAME_WIDTH,
            source_y,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
            0,
            flip,
            self.x,
            self.y,
            self.DRAW_WIDTH,
            self.DRAW_HEIGHT,
        )
