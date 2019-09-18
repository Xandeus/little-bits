import random
import pyautogui
from pynput.mouse import Listener
from collections import defaultdict
import pickle
import sys
import time

pyautogui.FAILSAFE = True
CLICK_POINTS = ["Three_Dot", "Add_Queue", "Remove_from_Playlist"]
global count
count = 0
# Config mode to tell program where to click
if len(sys.argv) > 1 and (sys.argv[1] == "-c" or sys.argv[1] == "--config"):
    set_positions = True
else:
    set_positions = False
    print("Click on window to start")
    with open('text_input_positions.pkl', 'rb') as input:
        text_position_data = pickle.load(input)

input_positions = defaultdict(dict)
dict_times = defaultdict(dict)


def queue_song(input_field_position):
    position = input_field_position[0]
    pyautogui.click(x=position[0], y=position[1])
    pyautogui.click(x=position[0], y=position[1])
    position = input_field_position[1]
    pyautogui.click(x=position[0], y=position[1])
    position = input_field_position[0]
    pyautogui.click(x=position[0], y=position[1])
    position = input_field_position[2]
    pyautogui.click(x=position[0], y=position[1])


def on_click(x, y, button, pressed):
    global count
    if set_positions:
        if not pressed:
            input_positions[count] = (x, y)
            count += 1
            # Stop listener
            if count >= len(CLICK_POINTS):
                with open('text_input_positions.pkl', 'wb') as output:
                    pickle.dump(input_positions, output, pickle.HIGHEST_PROTOCOL)
                return False

            print("Please click %s" % (CLICK_POINTS[count]))
    else:
        while True:
            queue_song(text_position_data)
            time.sleep(120)
        return False


# Collect events until released
with Listener(
         on_click=on_click,
         ) as listener:
     listener.join()

# print(input_positions)


