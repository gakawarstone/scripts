init 1 python:
    # import config as c
    def load_pers(name, closes):
        return "mods/gkmod/image/sprites/" + name + '/' + name + '_' + closes + ".png"

    def load_bg(_dir, name):
        return "mods/gkmod/image/bg/" + _dir +'/' + name ".jpg"

    def load_cg(_dir, name):
        return "mods/gkmod/image/cg/" + _dir + '/' + name ".jpg"
