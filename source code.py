
import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    [https://teams.microsoft.com/l/meetup-join/19%3aEkCxIm6KAd9PKzCIAO66aRNHfGXqJnHaxrdJBncKRPQ1%40thread.tacv2/1724491735068?context=%7b%22Tid%22%3a%2213a8d02d-59f3-416a-8231-b3080e639cad%22%2c%22Oid%22%3a%221a2eb5e5-b7d1-4304-951a-99aed00d3828%22%7d]
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(20)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','shift','m')
                time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break

                
