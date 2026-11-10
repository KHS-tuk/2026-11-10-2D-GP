from pico2d import load_image


class Bird:
    FRAME_WIDTH = 183
    FRAME_HEIGHT = 168
    FRAME_COUNT = 14
    IMAGE_WIDTH = 918
    IMAGE_HEIGHT = 506
    DRAW_WIDTH = 110
    DRAW_HEIGHT = 100

    image = None

    def __init__(self, x, y):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y
        self.frame = 0.0
        self.direction = 1
