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
