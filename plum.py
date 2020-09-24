class Plum:

    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

    def update(self, time_passed):
        self.y += self.speed * time_passed