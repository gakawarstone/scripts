init:

    $ mods["gk_story"]= "{font=mods/gkmod/image/font/font1.ttf}{size=45}{color=#92770a}Я непридумал название{/font}{/color}{/size}"

    $ mods["init_busket"]= "{font=mods/gkmod/image/font/font1.ttf}{size=45}{color=#92770a}Баскетболл{/font}{/color}{/size}"

    $ mods["day_1"]= "{font=mods/gkmod/image/font/font1.ttf}{size=45}{color=#92770a}День первый{/font}{/color}{/size}"

    $ mods["blpi_football"]= "{font=mods/gkmod/image/font/font1.ttf}{size=45}{color=#92770a}Футбол{/font}{/color}{/size}"

    #CHARACTERS
    $ thebest = Character (u'Рассказчик', color="FF4000", what_color="FFBF00")

    $ m6g = Character (u'Рома', color="FFBF00", what_color="FF4000")

    $ gcs = Character (u'Дибилы', color="FFBF00", what_color="FF006A")

    $ gws = Character (u'Вано', color="FF0000", what_color="FF006A")

    $ mkf = Character (u'Незнакомка', color="9C1056", what_color="FF00F7")

    $ tuw = Character (u'Гена', color="55FF00", what_color="3C00FF")

    $ dio = Character (u'Рустам', color="CC5500", what_color="128700")

    $ rei = Character (u'Dанил', color="9C0000", what_color="FFFFFF")

    $ mnk = Character (u'Моника', color="9C1056", what_color="FF00F7")

    $ mom = Character (u'Мама', color="9CCD56", what_color="FF0077")

    $ tel = Character (u'Телефон', color="FF0000", what_color="FF4000")

    $ lis = Character (u'Лиза', color="FF7370", what_color="9F5070")

#    $ aml = Character (u'Амелия', color="FF7370", what_color="9F5070")

    $ ant = Character (u'Антон', color="FF7370", what_color="9F5070")

    $ dan = Character (u'Денис', color="FF7370", what_color="9F5070")

    $ eva = Character (u'Ева', color="FF7370", what_color="9F5070")

    $ evl = Character (u'Эвелина', color="FF7370", what_color="9F5070")

    #BG
    image city = "mods/gkmod/image/bg/bg_prolog/city_aus.jpg"

    image shop_street = "mods/gkmod/image/bg/bg_prolog/shop_street.jpg"

    image shop = "mods/gkmod/image/bg/bg_prolog/shop_in_2.jpg"

    image bus_in = "mods/gkmod/image/bg/bg_prolog/pikdam_begin_busbus.jpg"

    image busket = "mods/gkmod/image/bg/bg_other/busket.jpg"

    #personality
    $ passive = 0
    $ active = 0

    #inventory
    $ inv = []

    #Have_seen var
    $ have_seen_gws = 0
    $ lie_gws = 0

    #inf var
    $ inf_nuts = 0

    #love var
    $ mnk_love = 0

    transform go_out_left:
        linear 0.5 xpos -0.3

    transform go_out_right:
        linear 0.5 xpos 1.3
