import random
import pyautogui
from pynput.mouse import Listener
from collections import defaultdict
import pickle
import sys

pyautogui.FAILSAFE = True
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIME_OF_DAY = ["Start_day", "Start_lunch", "End_lunch", "End_day"]
global count_time
global count_day
count_time = 0
count_day = 0
# Config mode to tell program where to click
if len(sys.argv) > 1 and (sys.argv[1] == "-c" or sys.argv[1] == "--config"):
    print("Please click %s box for %s" % (TIME_OF_DAY[count_time], DAYS[count_day]))
    set_positions = True
else:
    set_positions = False
    time_file = sys.argv[1]
    print("Using file: %s" % time_file)
    pyautogui.alert(text="Start entering time?")
    with open('text_input_positions.pkl', 'rb') as input:
        text_position_data = pickle.load(input)

input_positions = defaultdict(dict)
dict_times = defaultdict(dict)


def enter_schedule(input_field_position):
    with open(time_file, "r") as f:
        for line in f:
            clock_ins = line.split()
            dict_times[clock_ins[0]][clock_ins[1]] = clock_ins[2]
    for day_key in dict_times:
        for time_key in dict_times[day_key]:
            position = input_field_position[day_key][time_key]
            pyautogui.click(x=position[0], y=position[1])
            pyautogui.click(x=position[0], y=position[1])
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(str(dict_times[day_key][time_key]))
    exit(0)


def on_click(x, y, button, pressed):
    global count_time
    global count_day
    if set_positions:
        if not pressed:
            input_positions[DAYS[count_day]][TIME_OF_DAY[count_time]] = (x, y)
            count_time += 1
            if count_time >= 4:
                count_time = 0
                count_day += 1
            # Stop listener
            if count_day >= 7:
                with open('text_input_positions.pkl', 'wb') as output:
                    pickle.dump(input_positions, output, pickle.HIGHEST_PROTOCOL)
                return False

            print("Please click %s box for %s" % (TIME_OF_DAY[count_time], DAYS[count_day]))
    else:
        enter_schedule(text_position_data)
        return False


# Collect events until released
with Listener(
         on_click=on_click,
         ) as listener:
     listener.join()

# print(input_positions)


