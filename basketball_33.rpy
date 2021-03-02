init python:
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

    game = Game_busket()


label busket_game:
    scene busket
    me "Я бросаю мяч"
    $ man = 'you'
    if game.hit(man):
        $ score = game.score[man]
        me "попал у меня теперь [score]"
    else:
        me "промах"

    scene busket
    show gws_std at right with dissolve2
    gws "Я бросаю мяч"
    $ man = 'gws'
    if game.hit(man):
        $ score = game.score[man]
        gws "попал у меня теперь [score]"
    else:
        gws "промах"

    scene busket
    show dio_std at right with dissolve2
    dio "Я бросаю мяч"
    $ man = 'dio'
    if game.hit(man):
        $ score = game.score[man]
        dio "попал у меня теперь [score]"
    else:
        dio "промах"

    scene busket
    show rei_std at right with dissolve2
    rei "Я бросаю мяч"
    $ man = 'rei'
    if game.hit(man):
        $ score = game.score[man]
        rei "попал у меня теперь [score]"
    else:
        rei "промах"

    scene busket
    show m6g_std at right with dissolve2
    m6g "Я бросаю мяч"
    $ man = 'm6g'
    if game.hit(man):
        $ score = game.score[man]
        m6g "попал у меня теперь [score]"
    else:
        m6g "промах"

    jump busket_game
