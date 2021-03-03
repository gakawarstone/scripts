init 2 python:
    sprites_list = {
    'aml': ['pio'],
    'ant': ['cas', 'pio'],
    'gws': ['cas', 'pio'],
    'dio': ['cas', 'pio'],
    'rei': ['cas', 'pio'],
    'gen': ['cas', 'pio'],
    'lis': ['cas', 'pio'],
    'm6g': ['cas', 'pio'],
    'lis': ['cas', 'pio'],
    'aml': ['cas', 'pio'],
    'evl': ['cas', 'pio'],
    'kat': ['cas', 'pio'],
    'eva': ['cas', 'pio'],
    'kri': ['cas', 'pio'],
    'lik': ['cas', 'pio'],
    'mas': ['cas', 'pio'],
    'rit': ['cas', 'pio'],
    'ant': ['cas', 'pio'],
    'dan': ['cas', 'pio'],
    'kol': ['cas', 'pio'],
    'ily': ['cas', 'pio'],
    'lid': ['cas', 'pio'],
    'tim': ['cas', 'pio'],
    'm6g': ['jac', 'pio'],
    }

    for pers in sprites_list:
        for cloth in sprites_list[pers]:
            renpy.image(pers + '_' + cloth, Image(load_pers(pers, cloth)))


# image aml_pio = load_pers('aml', 'pio')
# image ant_cas = load_pers('ant', 'cas')
# image gws_std = load_pers('gws', 'std')
# image rei_std = load_pers('rei', 'std')
# image gen_std = load_pers('gen', 'std')
# image dio_std = load_pers('dio', 'std')
