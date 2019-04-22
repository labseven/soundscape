# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
from os import listdir
import subprocess
import board
import digitalio

button_pins = [board.D22, board.D23, board.D24, board.D27]
buttons = []

for pin in button_pins:
    buttons.append(digitalio.DigitalInOut(pin))
    buttons[-1].direction = digitalio.Direction.INPUT
    buttons[-1].pull = digitalio.Pull.UP

mp3_files = [ f for f in listdir('../assets/') if f[-4:] == '.mp3' ]


if not len(mp3_files) > 0:
    print("No mp3 files found!")
else:
    print('--- Available mp3 files ---')
    print(mp3_files)

isPlaying = -1

def processPlugIn(buttonIndex):
    global isPlaying
    if(isPlaying is not buttonIndex):
        subprocess.call(['killall', 'omxplayer.bin'])
        subprocess.Popen(['omxplayer', '-o', 'local', '/home/pi/Documents/soundscape/assets/'+ mp3_files[buttonIndex-1]])
        isPlaying = buttonIndex
        print('--- Playing ' + mp3_files[buttonIndex-1] + ' ---')
        time.sleep(0.25)

def processPlugOut(buttonIndex):
    global isPlaying
    subprocess.call(['killall', 'omxplayer.bin'])
    print('--- Stopping ' + mp3_files[buttonIndex-1] + ' ---')
    isPlaying = -1
    time.sleep(0.25)

while True:
    if isPlaying == -1:
        for i, button in enumerate(buttons):
            if (not button.value):
                processPlugIn(i) 
    elif buttons[isPlaying].value:
        processPlugOut(i)
      
    time.sleep(0.25)
