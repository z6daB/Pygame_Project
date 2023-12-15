dict_screens = {}

current_screen = None

def get_current_screen():
    return current_screen

def ChangeScreen(screen_name):
    global current_screen
    current_screen = dict_screens[screen_name]
    print(screen_name)