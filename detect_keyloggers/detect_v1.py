import time
import os
import sys
from pathlib import Path


def get_path():
    if sys.platform.startswith('win'):
        base = Path(os.getenv('APPDATA', str(Path.home())))
        path = base / 'Microsoft' / 'Windows' / 'Logs'
    elif sys.platform.startswith('linux'):
        path = Path('/tmp')
    else:
        path = Path.home()
    return path


directory = get_path()
delay = 300

print(f'[*] Analyse of {directory}')
print(f'[*] Limit of suspicion : {delay}')

now = time.time()

for file in directory.iterdir():
    if not file.name.startswith('.'):
        continue

    age = now - file.stat().st_mtime

    if age < delay:
        print(f'[ALERT] Hidden file has been modified {int(age)}s ago : {file}')
    else:
        print(f'[OK] Old hidden file ({int(age)}) : {file}')


