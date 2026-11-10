from pico2d import get_canvas_width

from bird import Bird


class BirdFlock:
    BIRD_COUNT = 10
    LEFT_LIMIT = Bird.DRAW_WIDTH / 2

    def __init__(self):
        self.birds = [
            Bird(
                180 + index * 130,
                410 + (index % 2) * 35,
                1 if index % 2 == 0 else -1,
            )
            for index in range(self.BIRD_COUNT)
        ]

    def update(self):
        for bird in self.birds:
            bird.update()
            if bird.x >= get_canvas_width() - self.LEFT_LIMIT:
                bird.x = get_canvas_width() - self.LEFT_LIMIT
                bird.direction = -1
            elif bird.x <= self.LEFT_LIMIT:
                bird.x = self.LEFT_LIMIT
                bird.direction = 1

    def draw(self):
        for bird in self.birds:
            bird.draw()
