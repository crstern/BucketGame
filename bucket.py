class Bucket:
    def __init__(self, speed=0.1, x=500, y=800):
        self.speed = speed
        self.x = x
        self.y = y
        self.move_right = 0
        self.move_left = 0

    def update(self, time_passed):
        if self.move_right:
            self.speed += self.speed * time_passed
        if self.move_left:
            self.speed -= self.speed * time_passed