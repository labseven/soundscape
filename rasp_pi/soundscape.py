# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
from os import listdir
import subprocess
import board
import digitalio

button1 = digitalio.DigitalInOut(board.D22)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D23)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D24)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D27)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

mp3_files = [ f for f in listdir('../assets/') if f[-4:] == '.mp3' ]


if not len(mp3_files) > 0:
    print("No mp3 files found!")
else:
    print('--- Available mp3 files ---')
    print(mp3_files)

isPlaying = 0

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
    isPlaying = 0
    time.sleep(0.25)

while True:
    # if the user plugs-out
    if (button1.value) and isPlaying == 1:
        processPlugOut(1)
    # if button2.value and isPlaying == 2:
    #     processPlugOut(2)
    # if button3.value and isPlaying == 3:
    #     processPlugOut(3)
    # if button4.value and isPlaying == 4:
    #     processPlugOut(4)
    # if the user plugs-in
    if (not button1.value) and isPlaying != 1:
        processPlugIn(1);
    # if (not button2.value) and isPlaying != 2:
    #     processPlugIn(2);
    # if (not button3.value) and isPlaying != 3:
    #     processPlugIn(3);
    # if (not button4.value) and isPlaying != 4:
    #     processPlugIn(4); 

    # if the user plugs-out       
    time.sleep(0.25)
