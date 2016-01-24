from gpiozero import *
from time import sleep

LedName = {}
LedName[1] = PWMLED(14,10)
LedName[1].on()
sleep(2)
led = LED(14)
led.on()
sleep(1)
