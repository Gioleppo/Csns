import math
import random

class Burgler:
    def steal(self, attractiveness, dt):
        pBurg = 1 - math.exp(- attractiveness*dt)
        if random.random() < pBurg :
            return True
        else:
            return False