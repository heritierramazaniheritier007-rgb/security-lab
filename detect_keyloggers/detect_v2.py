import os
from pathlib import Path

SUSPECT_DIRS = ['/tmp', '/dev/shm', '/var/tmp']

print('[*] Scan Python processes\n')

for pid_dir in Path('/proc').iterdir():
    if not pid_dir.name.isdigit():
        continue
    cmdline_file = pid_dir / 'cmdline'
    if not cmdline_file.exists():
        continue

    try:
        raw = cmdline_file.read_bytes()
    except (PermissionError, FileNotFoundError):
        continue
    if not raw:
        continue

    cmdline = raw.replace(b'\x00', b' ').decode(errors='ignore').strip()

    if 'python' not in cmdline.lower():
        continue

    cwd_link = pid_dir / 'cwd'
    try:
        cwd = os.readlink(cwd_link)
    except (PermissionError, FileNotFoundError):
        cwd = '?'

    suspect = False
    for d in SUSPECT_DIRS:
        if cwd.startswith(d):
            suspect = True

    tag = '[ALERT]' if suspect else '[OK]'
    print(f'{tag} PID={pid_dir} cwd={cwd}')
    print(f'          cmd: {cmdline}\n')


