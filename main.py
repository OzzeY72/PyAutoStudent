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

def setup_connectfinal_cord(settings):
     while True:
        if keyboard.is_pressed('ctrl+h'):
            coordinates = pyautogui.position()
            settings['connectfinal_cord_x'] = coordinates.x
            settings['connectfinal_cord_y'] = coordinates.y

            with open('settings.json', 'w') as f:
                json.dump(settings, f)

            print(settings['connectfinal_cord_x'],settings['connectfinal_cord_y'])
            break
        elif keyboard.is_pressed('q'):
            break

def join(settings):
    pyautogui.click(settings['join_cord_x'],settings['join_cord_y'])

def connect(settings):
    pyautogui.click(settings['connect_cord_x'],settings['connect_cord_y'])

def connectfinal(settings):
    pyautogui.click(settings['connectfinal_cord_x'],settings['connectfinal_cord_y'])

def check_videocheckbox(settings):
    #im = pyautogui.screenshot()
    #px = im.getpixel((settings['videocheckbox_cord_x'],settings['videocheckbox_cord_y']))
    #if not ((px[0] == 14 and px[1] == 113 and px[2] == 235) or (px[0] > 250 and px[1] > 250 and px[2] > 250)):
    pyautogui.click(settings['videocheckbox_cord_x'],settings['videocheckbox_cord_y'])

def write_code(code):
    pyautogui.write(code)

async def main():
    avg_latency = 1
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
        setup_connectfinal_cord(settings)
    else:
        #Action block
        await asyncio.sleep(avg_latency)
        join(settings)
        await asyncio.sleep(avg_latency)
        write_code(meets["zoom"][0]['code'])
        check_videocheckbox(settings)
        await asyncio.sleep(avg_latency)
        connect(settings)
        await asyncio.sleep(3*avg_latency)
        #Enter pass from conf
        write_code(meets["zoom"][0]['pass'])
        #Click connect to meet button
        connectfinal(settings)

        p.terminate()

asyncio.run(main())
