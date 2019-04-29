# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
from os import listdir
import os
import board
import digitalio
import pygame

button_pins = [board.D2, board.D3, board.D4, board.D17, board.D23, board.D24]
buttons = []

for pin in button_pins:
    buttons.append(digitalio.DigitalInOut(pin))
    buttons[-1].direction = digitalio.Direction.INPUT
    buttons[-1].pull = digitalio.Pull.UP

wav_files = [ f for f in listdir('../assets/') if f[-4:] == '.wav' ]

if not len(wav_files) > 0:
    print("No wav files found!")
else:
    print('--- Available wav files ---')
    print(wav_files)

dirname = os.path.dirname(__file__)
# init mixer and load sounds

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

# pygame Sounds Object has limited mp3 support, using wav files for everything
print("Loading sounds file..")
start = time.time()
# ordered from right to left, from T-station to School
sounds = []

print("Loading t_station..")
t_station = pygame.mixer.Sound('../assets/t_station.wav')
sounds.append(t_station)
print("Loading walking..")
walking = pygame.mixer.Sound('../assets/walking.wav')
sounds.append(walking)
print("Loading park..")
park = pygame.mixer.Sound('../assets/park.wav')
sounds.append(park)
print("Loading bakery..")
bakery = pygame.mixer.Sound('../assets/bakery.wav')
sounds.append(bakery)
print("Loading barber_shop..")
barber_shop = pygame.mixer.Sound('../assets/barber_shop.wav')
sounds.append(barber_shop)

# dummy
sounds.append(barber_shop)
sounds.append(barber_shop)


# not enough memory on rasp_pi
# print("Loading birds..")
# sounds.append(pygame.mixer.Sound('../assets/birds.wav'))
# print("Loading kids..")
# sounds.append(pygame.mixer.Sound('../assets/kids.wav'))


end = time.time()
print("Loading sounds complete, Elapsed Time :", end - start )

isPlaying = -1

def processPlugIn(buttonIndex):
    global isPlaying
    pygame.mixer.stop()
    pygame.mixer.Channel(buttonIndex).play(sounds[buttonIndex])
    isPlaying = buttonIndex
    print('--- Playing ' + wav_files[buttonIndex] + ' ---')
    time.sleep(0.25)

def processPlugOut(buttonIndex):
    global isPlaying
    print('--- plugged out button : ', buttonIndex)
    pygame.mixer.stop()
    print('--- Stopping ' + wav_files[buttonIndex] + ' ---')
    isPlaying = -1
    time.sleep(0.25)

while True:
    if isPlaying == -1:
        for i, button in enumerate(buttons):
            if button.value:
                processPlugIn(i) 
    elif not buttons[isPlaying].value:
        processPlugOut(isPlaying)
        
    time.sleep(0.25)
