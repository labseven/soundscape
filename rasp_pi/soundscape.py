# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
from os import listdir
import subprocess
import board
import digitalio

button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D24)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

# button3 = digitalio.DigitalInOut(board.D25)
# button3.direction = digitalio.Direction.INPUT
# button3.pull = digitalio.Pull.UP

mp3_files = [ f for f in listdir('../assets/') if f[-4:] == '.mp3' ]


if not len(mp3_files) > 0:
    print("No mp3 files found!")

print('--- Available mp3 files ---')
print(mp3_files)

isPlaying = False
btnList = [button1, button2]

def resetButtonValuesExcept(exceptButton):
    for button in btnList:
        if button != exceptButton:
            button.value = True
            print("resetting %s", button)
    subprocess.call(['killall', 'omxplayer'])
    print('--- Cleared all existing mp3s. ---')




while True:

    if not button1.value:
        if(isPlaying):
            resetButtonValuesExcept(button1) 
        subprocess.Popen(['omxplayer', '-o', 'local', '../assets/'+ mp3_files[0]])
        isPlaying = True
        print('--- Playing ' + mp3_files[0] + ' ---')
        time.sleep(0.25)

    if not button2.value:
        if(isPlaying):
            resetButtonValuesExcept(button1)
        subprocess.Popen(['omxplayer', '-o', 'local', '../assets/'+ mp3_files[1]])
        isPlaying = True
        print('--- Playing ' + mp3_files[1] + ' ---')
        time.sleep(0.25)

    time.sleep(0.25)
