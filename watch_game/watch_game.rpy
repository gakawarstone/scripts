init 10:
    image paper_watch = load_from("watch_game", "background", end=".png")

    python:
        for i in range(13):
            renpy.image('paper_watch_' + str(i), Image(load_from("watch_game", str(i), end=".png")))
