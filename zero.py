from gpiozero import LED
from time import sleep

LedName = {}
LedName[1] = LED(14)
print(LedName[1])
LedName[1].on()
sleep(5)
