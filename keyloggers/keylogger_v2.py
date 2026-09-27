import os
import sys
import datetime
from pathlib import Path


def get_log_path():
    if sys.platform.startswith('win'):
        base = Path(os.getenv('APPDATA', str(Path.home())))
        directory = base / 'Microsoft' / 'Windows' / 'Logs'
    elif sys.platform.startswith('linux'):
        directory = Path('/temp')
    else:
        directory = Path.home()

    directory.mkdir(parents=True, exist_ok=True)
    return directory / '.cache_sys.log'


def write_log(text):
    path = get_log_path()
    now = datetime.datetime.now()
    formated = now.strftime('%d-%m-%Y %H:%M:%S')

    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'[{formated}] {text}\n')


write_log('First line')
write_log('Second line')
write_log('Third line')

