from gpiozero import PWMLED
from time import sleep

LedName = {}
LedName[1] = PWMLED(14,10)
LedName[1].on()
sleep(5)
