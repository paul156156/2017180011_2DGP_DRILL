import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYUP and event.key == SDLK_p:
            game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(10, 10)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






