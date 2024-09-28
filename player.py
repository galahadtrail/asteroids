from circleshape import *
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0