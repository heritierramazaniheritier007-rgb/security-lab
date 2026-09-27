"""
import datetime

with open('file_1.txt', 'a') as f:
    now = datetime.datetime.now()
    formated = now.strftime('%d-%m-%Y a %H:%M:%S')
    f.write(f'mkdir directory : {formated}\n')

"""
from pathlib import Path
import os

directory = Path('C:/Users/05032004/Desktop')
file = directory / 'my_log.txt'
# print(file)

print(os.getenv('APPDATA'))


