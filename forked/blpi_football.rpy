init 200 python:
    blpi_football_text = [
        "Мяч летит в верхний левый угол! Практически под перекладину!",
        "Сильный удар низом в левую сторону. Пры-ы-ыжок!",
        "Кручёный мяч летит по центру ворот. Скорее всего под перекладину!",
        "Удар низом по центру. Успеть бы!",
        "Очень сильный удар в правый верхний угол!",
        "Низкий и плотный удар низом вправо!"
                        ]

    blpi_otbil_text = [
        ["Нелепо выпрыгнув вперёд, я движеним руки отразил адресованный мне мяч.",
            "Он же с характерным звоном отлетел чуть за край поля и останавился в \"ауте\".",
            "~Вот там и оставайся, негодяй!~",
            "Я мысленно сложил все предыдущие попытки взятия моих ворот и спокойно выдохнул:",
            "Отведенные мне 5 ударов были сделаны.",
            "Я устало снял перчатки."],
        ["Капля холодного пота прокатилась по спине, оставляя после себя неприятное ощущение прохлады.",
            "Отбил!",
            "~Да сколько же там еще ударов?~"],
        ["Извернувшись подобно кошке, я одним движением \"лапы\" стал владельцем мяча.",
            "Оставалось всего 2 удара!",
            "~Давай, Сеня! Ты можешь!~"],
        ["Подскочив к летящему на встречу мячу, я молниеносным движением стал непреодолимой стеной между полем и воротами.",
            "Второй штурм охраняемых мною ворот был отбит!",
            "~Мужайся, осталось всего 3 удара!~"],
        ["Отпружинив от резиновых рукавиц, мяч плавно опустился на землю рядом со мной.",
            "Первый удар был отбит. Оставалось еще четыре..."]
                    ]

    blpi_miss_text =[
        ["Всё! Я больше не могу!",
            "Судя по статистике, которую я вёл у себя в голове, это был последний из предназначенных мне ударов.",
            "Я устало снял перчатки."],
        ["Судя по количеству ударов, это был предпоследний удар.",
            "Мяч же плавно прокатился по сетке ворот и издеваючи ударился о мою ногу.",
            "Последний удар!"],
        ["Да чтож такое?! Пропустил!",
            "Обернувшись назад, я взглянул на мяч обиженным и злым взглядом.",
            "Будто это он виноват в моём провале.",
            "~Сеня! Соберись!~",
            "Еще 2 удара."],
        ["Гол!",
            "Обычно, это слово произносят громко и радостно. Но только не вратари...",
            "Я впервые в жизни задумался, что для любого вратаря слово \"гол\" одновременно и обожаемо и ненавидимо...",
            "Однако, времени на рассуждения у меня не осталось. Еще 3 удара!"],
        ["Первый же удар пролетел в паре сантиметров от моей руки.",
            "Мяч упруго пронзил воротную сетку, однако через мгновение упал, будто ставя точку в предложении:",
            "\"Ты пропустил гол, Семён.\"",
            "Так, ладно. Нужно собраться!"]
                ]

    blpi_footblall_coords = [
        [195,129,384,359],
        [188,656,405,390],
        [784,110,360,341],
        [801,720,364,293],
        [1334,135,391,395],
        [1329,647,381,403]
                            ]

    blpi_goal_c = 0
    blpi_num = 5
    blpi_cell = str()
    blpi_cell_n = int()
    def blpi_calc_blpi_cell():
        blpi_cell_n = renpy.random.randint(0,5)
        blpi_cell = blpi_football_text[blpi_cell_n]
        return blpi_cell, blpi_cell_n

    def blpi_otbil(i):
        global blpi_cell_n, blpi_goal_c, blpi_num
        blpi_num-=1
        if i == blpi_cell_n:
            blpi_goal_c += 1
            renpy.jump("blpi_lb_otbil")
        else:
            renpy.jump("blpi_lb_miss")
        return

    def blpi_countdown(st, at, length=0.0):
        remaining = length - st
        if remaining > 2.0:
            return Text("%.1f" % remaining, color="#fff", size=70), .1
        elif remaining > 0.0:
            return Text("%.1f" % remaining, color="#dd2323", size=70), .1
        else:
            return anim.Blink(Text("0.0", color="#dd2323", size=70)), None

    for i in range(1, 6):
        renpy.image('blpi_countdown' + str(i), DynamicDisplayable(blpi_countdown, length=i))

label blpi_football:
    python:
        #mouse_visible = False
        renpy.scene()
        renpy.show('blpi_gate_i')
        if blpi_num == 0:
            renpy.jump('blpi_itog')
        blpi_cell, blpi_cell_n = blpi_calc_blpi_cell()
        renpy.pause(1.0, hard=True)
        narrator(blpi_cell + "{w=2}{nw}")
        renpy.block_rollback()
        renpy.set_mouse_pos(960,1070)
        #mouse_visible = True
        renpy.call_screen('blpi_football_sc')

screen blpi_football_sc:
    imagemap:
        ground 'blpi_gate_i'
        hover 'blpi_gate_h'
        for i in range(6):
            hotspot (
            blpi_recalculation_function_x(blpi_footblall_coords[i][0]),
            blpi_recalculation_function_y(blpi_footblall_coords[i][1]),
            blpi_recalculation_function_x(blpi_footblall_coords[i][2]),
            blpi_recalculation_function_y(blpi_footblall_coords[i][3])
            ) action Function(blpi_otbil, i)

    if blpi_num > 0:
        add "blpi_countdown"+str(blpi_num) xalign 0.5 yalign 0.5
        timer blpi_num action Hide("blpi_football_sc"), Jump("blpi_tie_out")
    text str(blpi_goal_c) size 70 xalign .98 yalign .03


label blpi_lb_otbil:
    $ renpy.block_rollback()
    hide screen blpi_football_sc
    scene blpi_gate_i
    play sound sfx_soccer_ball_catch
    python:
        for i in blpi_otbil_text[blpi_num]:
            narrator(i)
    jump blpi_football

label blpi_lb_miss:
    $ renpy.block_rollback()
    hide screen blpi_football_sc
    scene blpi_gate_i
    play sound sfx_soccer_ball_gate
    python:
        for i in blpi_miss_text[blpi_num]:
            narrator(i)
    jump blpi_football

label blpi_tie_out:
    $ renpy.block_rollback()
    hide screen blpi_football_sc
    scene blpi_gate_i
    $ blpi_num-=1
    play sound sfx_soccer_ball_gate
    "~Эх... Пропустил...~"
    "Мяч, как песок сквозь пальцы, проскочил в нескольких сантиметрах от моей руки и ..."
    "... с легким звоном, скатился по закрывающей сзади ворота мягкой сетке."
    "~Надо собраться!~"
    jump blpi_football

label blpi_itog:
    $ renpy.block_rollback()
    hide screen blpi_football_sc
    $ mouse_visible = True
    scene blpi_bg ext_playground_sunset with Fade(1.5,0,1.5)
    "Вышло так, что из пяти ударов я смог отбить [blpi_goal_c]."
    if blpi_goal_c == 3:
        "Неплохо. Учитывая, что стоять в воротах мне не приходилось о-о-о-очень давно."
    elif blpi_goal_c == 4:
        "Весьма недурно. Только вот этот один пропущенный гол портил мою идеальную статистику."
    elif blpi_goal_c == 5:
        "Я просто вратарский гений."
    $ blpi_prev_location = "footbal"
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    play ambience ambience_camp_entrance_evening fadein 3.0
    return
