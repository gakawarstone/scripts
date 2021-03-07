import random

class Game_busket:
    def __init__(self):
        self.score = {
        'gws': 0,
        'dio': 0,
        'rei': 0,
        'm6g': 0,
        'you': 0,
        }

        self.skill_2x = {
        'gws': 80,
        'dio': 70,
        'rei': 65,
        'm6g': 60,
        'you': 55,
        }

        self.skill_3x = {
        'gws': 20,
        'dio': 18,
        'rei': 10,
        'm6g': 10,
        'you': 8,
        }


    def check_hit_2x(self, man):
        if self.skill_2x[man] >= random.randint(0, 100):
            return True
        else:
            return False


    def check_hit_3x(self, man):
        if self.skill_3x[man] >= random.randint(0, 100):
            return True
        else:
            return False

    def hit(self, man):
        if self.score[man] >= 30 and self.check_hit_3x(man):
            self.score[man] += 1
            return True

        elif self.check_hit_2x(man):
            self.score[man] += 2
            return True

        else:
            return False
