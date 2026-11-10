from pico2d import load_image

import game_framework


class Bird:
    FRAME_COUNT = 14
    IMAGE_HEIGHT = 506
    FRAME_X = (0, 183, 366, 549, 732)
    FRAME_X_END = (183, 366, 549, 732, 918)
    FRAME_Y = (0, 169, 338)
    FRAME_Y_END = (169, 338, 506)
    DRAW_WIDTH = 110
    DRAW_HEIGHT = 100
    FRAMES_PER_SECOND = 12.0
    SPEED = 180.0

    image = None

    def __init__(self, x, y, direction=1):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y
        self.frame = 0.0
        self.direction = direction

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
        source_x = self.FRAME_X[column]
        source_width = self.FRAME_X_END[column] - source_x
        source_y = self.IMAGE_HEIGHT - self.FRAME_Y_END[row]
        source_height = source_y - self.FRAME_Y[row]
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            source_x,
            source_y,
            source_width,
            source_height,
            0,
            flip,
            self.x,
            self.y,
            self.DRAW_WIDTH,
            self.DRAW_HEIGHT,
        )
