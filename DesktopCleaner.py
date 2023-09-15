import shutil
import os

screenshot_dir = '/Users/till/Desktop/ScreenShots'
desktop_dir = '/Users/till/Desktop'

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print('Creating ScreenShots folder ...')

files_on_desktop = os.listdir(desktop_dir)

for file in files_on_desktop:
    if file.startswith('Screenshot'): # and file.endswith('.png')
        file_dir = desktop_dir + '/' + file
        shutil.move(file_dir, screenshot_dir)
        print(f'Moving {file} ...') 

