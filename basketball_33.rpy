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
            'gws': 78,
            'dio': 60,
            'rei': 57,
            'm6g': 55,
            'you': 50,
            }

            self.skill_3x = {
            'gws': 30,
            'dio': 16,
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
            """
            if self.score[man] >= 30 and self.check_hit_3x(man):
                self.score[man] += 1
                return True

            elif self.check_hit_2x(man):
                self.score[man] += 2
                return True

            else:
                return False
            """
            if self.check_hit_2x(man) and self.score[man] < 30:
                if self.score[man] < 30:
                    self.score[man] += 2
                    return True
            elif self.score[man] >= 30 and self.check_hit_3x(man):
                    self.score[man] += 1
                    return True
            else:
                return False


label init_busket():
    $ game = Game_busket()


label busket_game:
    $ renpy.block_rollback()
    scene busket
    me "Я бросаю мяч"
    $ man = 'you'
    if game.hit(man):
        $ score = game.score[man]
        me "попал у меня теперь [score]"
    else:
        me "промах"
    if game.score[man] == 33:
        me "Я выйграл"
        return

    scene busket
    show gws_pio at right with dissolve
    gws "Я бросаю мяч"
    $ man = 'gws'
    if game.hit(man):
        $ score = game.score[man]
        gws "попал у меня теперь [score]"
    else:
        gws "промах"
    if game.score[man] == 33:
        gws "Я выйграл"
        return

    scene busket
    show dio_pio at right with dissolve
    dio "Я бросаю мяч"
    $ man = 'dio'
    if game.hit(man):
        $ score = game.score[man]
        dio "попал у меня теперь [score]"
    else:
        dio "промах"
    if game.score[man] == 33:
        dio "Я выйграл"
        return

    scene busket
    show rei_pio at right with dissolve
    rei "Я бросаю мяч"
    $ man = 'rei'
    if game.hit(man):
        $ score = game.score[man]
        rei "попал у меня теперь [score]"
    else:
        rei "промах"
    if game.score[man] == 33:
        rei "Я выйграл"
        return

    scene busket
    show m6g_jac at right with dissolve
    m6g "Я бросаю мяч"
    $ man = 'm6g'
    if game.hit(man):
        $ score = game.score[man]
        m6g "попал у меня теперь [score]"
    else:
        m6g "промах"
    if game.score[man] == 33:
        m6g "Я выйграл"
        return

    jump busket_game
