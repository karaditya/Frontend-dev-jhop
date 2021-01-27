import pyautogui as pg
import numpy as np
import time

pg.FAILSAFE = True

# Text messages to save
W = input('Enter Word Text:')
N = input('Enter Notepad Text:')

# Open Notepad
pg.hotkey('winleft')
time.sleep(1)
pg.write('notepad')
pg.press('enter')
time.sleep(1)

# Open Wordpad
pg.hotkey('winleft')
time.sleep(1)
pg.write('word')
time.sleep(1)
pg.press('enter')

time.sleep(5)

# Close button click
pg.click(x=1002, y=680)
time.sleep(1)

# Open blank document
pg.click(x=603, y=317)
time.sleep(2)

# Write & Save Text
pg.write(W)
pg.hotkey('ctrl','s')
time.sleep(2)
pg.click(x=322, y=287)
time.sleep(1)
pg.click(x=684, y=281)
time.sleep(2)
pg.write('file'+str(np.random.randint(0,1000)))
pg.press('enter')

# GoTo Notepad and Write & Save Text
pg.hotkey('alt','tab')
time.sleep(1)
pg.write(N)
pg.hotkey('ctrl','s')
pg.write('file'+str(np.random.randint(0,1000)))
pg.press('enter')

print('Success')

