import pyautogui
import keyboard
from subprocess import Popen
import json
import time
import asyncio

#Settings block
def setup_join_cord(settings):
    while True:
        if keyboard.is_pressed('ctrl+j'):
            settings['first_launch'] = False
            coordinates = pyautogui.position()
            settings['join_cord_x'] = coordinates.x
            settings['join_cord_y'] = coordinates.y

            with open('settings.json', 'w') as f:
                json.dump(settings, f)

            print(settings['join_cord_x'],settings['join_cord_y'])

            break
        elif keyboard.is_pressed('q'):
            break

def setup_videocheckbox_cord(settings):
     while True:
        if keyboard.is_pressed('ctrl+h'):
            coordinates = pyautogui.position()
            settings['videocheckbox_cord_x'] = coordinates.x
            settings['videocheckbox_cord_y'] = coordinates.y

            with open('settings.json', 'w') as f:
                json.dump(settings, f)

            print(settings['videocheckbox_cord_x'],settings['videocheckbox_cord_y'])

            break
        elif keyboard.is_pressed('q'):
            break

def setup_connect_cord(settings):
     while True:
        if keyboard.is_pressed('ctrl+j'):
            coordinates = pyautogui.position()
            settings['connect_cord_x'] = coordinates.x
            settings['connect_cord_y'] = coordinates.y

            with open('settings.json', 'w') as f:
                json.dump(settings, f)

            print(settings['connect_cord_x'],settings['connect_cord_y'])
            break
        elif keyboard.is_pressed('q'):
            break

def join(settings):
    pyautogui.click(settings['join_cord_x'],settings['join_cord_y'])

def connect(settings):
    pyautogui.click(settings['connect_cord_x'],settings['connect_cord_y'])

def check_videocheckbox(settings):
    im = pyautogui.screenshot()
    px = im.getpixel((settings['videocheckbox_cord_x'],settings['videocheckbox_cord_y']))
    if not ((px[0] == 14 and px[1] == 113 and px[2] == 235) or (px[0] > 250 and px[1] > 250 and px[2] > 250)):
        pyautogui.click(settings['videocheckbox_cord_x'],settings['videocheckbox_cord_y'])

def write_code(meets):
    pyautogui.write(meets["zoom"][0]['code'])

async def main():
    settings_file = open('settings.json') 
    settings = json.load(settings_file)
    settings_file.close()
    meets_file = open('meets.json')
    meets = json.load(meets_file)
    print(settings)
    
    p = Popen([settings['path']]) 
    #await subprocess.call([settings['path']])
    #Settings block
    if settings['first_launch']:    
        setup_join_cord(settings)
        setup_videocheckbox_cord(settings)
        setup_connect_cord(settings)
    #Action block
    await asyncio.sleep(7)
    join(settings)
    await asyncio.sleep(7)
    write_code(meets)
    check_videocheckbox(settings)
    await asyncio.sleep(2)
    connect(settings)
    await asyncio.sleep(12)
    p.terminate()

asyncio.run(main())
