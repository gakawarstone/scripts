init 3 python:
    """
    speakers_list = {
    'aml': ['Амелия', '#FFFFFF', '#FFFFFF']
    }

    global DynamicCharacter
    gl = globals()
    for name in speakers_list.keys():
        gl[name] = DynamicCharacter(speakers_list[name][0], color=speakers_list[name][1], what_color=speakers_list[name][2])
    """

    aml = Character('Амелия', color='#FFFFFF')
    gen = Character('Геннадий', color='#FDA546')
    ily = Character('Илья', color='#48D4B2')
    kat = Character('Катя', color='#48D4B2')
    kri = Character('Кристина', color='#48D4B2')
    lid = Character('Лида', color='#48D4B2')
    kol = Character('Коля', color='#48D4B2')
    lis = Character('Лиза', color='#48D4B2')
    lik = Character('Лика', color='#48D4B2')
    mas = Character('Маша', color='#48D4B2')
    mnc = Character('Моника', color='#48D4B2')
    rit = Character('Рита', color='#48D4B2')
    tim = Character('Тимур', color='#48D4B2')
    fmn = Character('Физрук', color='#48D4B2')
