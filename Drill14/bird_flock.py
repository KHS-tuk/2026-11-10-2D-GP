from bird import Bird


class BirdFlock:
    BIRD_COUNT = 10

    def __init__(self):
        self.birds = [
            Bird(180 + index * 130, 410 + (index % 2) * 35)
            for index in range(self.BIRD_COUNT)
        ]

    def update(self):
        for bird in self.birds:
            bird.update()

    def draw(self):
        for bird in self.birds:
            bird.draw()
