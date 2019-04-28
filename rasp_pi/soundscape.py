# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
from os import listdir
import os
# import board
# import digitalio
import pygame

# button_pins = [board.D22, board.D23, board.D24, board.D27]
buttons = []

# for pin in button_pins:
#     buttons.append(digitalio.DigitalInOut(pin))
#     buttons[-1].direction = digitalio.Direction.INPUT
#     buttons[-1].pull = digitalio.Pull.UP

ogg_files = [ f for f in listdir('../assets/') if f[-4:] == '.ogg' ]

if not len(ogg_files) > 0:
    print("No ogg files found!")
else:
    print('--- Available ogg files ---')
    print(ogg_files)

dirname = os.path.dirname(__file__)
# init mixer and load sounds

pygame.mixer.init()
# pygame Sounds Object has limited mp3 support, using ogg files for everything
print("Loading sounds file..")
start = time.time()
# ordered from right to left, from T-station to School
sounds = []
print("Loading t_station..")
sounds.append(pygame.mixer.Sound('../assets/t_station.ogg'))
print("Loading walking..")
sounds.append(pygame.mixer.Sound('../assets/walking.ogg'))
print("Loading park..")
sounds.append(pygame.mixer.Sound('../assets/park.ogg'))
print("Loading bakery..")
sounds.append(pygame.mixer.Sound('../assets/bakery.ogg'))
print("Loading barber_shop..")
sounds.append(pygame.mixer.Sound('../assets/barber_shop.ogg'))
print("Loading birds..")
# sounds.append(pygame.mixer.Sound('../assets/birds.ogg'))
print("Loading kids..")
sounds.append(pygame.mixer.Sound('../assets/kids.ogg'))

end = time.time()
print("Loading sounds complete, Elapsed Time :", end - start )


# pygame.mixer.Channel(0).play(sounds[0])


isPlaying = -1

# def processPlugIn(buttonIndex):
#     global isPlaying
#     subprocess.call(['killall', 'omxplayer.bin'])
#     subprocess.Popen(['omxplayer', '-o', 'local', '/home/pi/Documents/soundscape/assets/'+ mp3_files[buttonIndex]])
#     isPlaying = buttonIndex
#     print('--- Playing ' + ogg_files[buttonIndex] + ' ---')
#     time.sleep(0.25)

# def processPlugOut(buttonIndex):
#     global isPlaying
#     print('--- plugged out button : ', buttonIndex)
#     subprocess.call(['killall', 'omxplayer.bin'])
#     print('--- Stopping ' + ogg_files[buttonIndex] + ' ---')
#     isPlaying = -1
#     time.sleep(0.25)

# while True:
#     if isPlaying == -1:
#         for i, button in enumerate(buttons):
#             if button.value:
#                 processPlugIn(i) 
#     elif not buttons[isPlaying].value:
#         processPlugOut(isPlaying)
        
#     time.sleep(0.25)
