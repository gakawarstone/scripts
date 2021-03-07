init 1 python:
    # import config as c
    main_dir = "mods/gkmod/image/"
    def load_pers(name, closes):
        return main_dir + "sprites/" + name + '/' + name + '_' + closes + ".png"

    def load_bg(_dir, name, end=".jpg"):
        return main_dir + "bg/" + _dir +'/' + name + end

    def load_cg(_dir, name, end=".jpg"):
        return main_dir + "cg/" + _dir + '/' + name + end

    def load_from(_dir, name, end=".jpg"):
        return main_dir + _dir + '/' + name + end
