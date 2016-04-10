import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause
from time import sleep

pin = int(input("pin:\t"))
pygame.mixer.init()

button = Button(pin)
drum = Sound("samples/drum_tom_mid_hard.wav")
while True:
    button.wait_for_press()
    print("button pressed")
    drum.play()
    sleep(0.1)
    button.wait_for_release()	
