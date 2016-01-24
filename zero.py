from gpiozero import LED
from time import sleep

LedName = {2:print("gio")}
LedName[1] = LED(14)
print(LedName)
LedName[2]
LedName[1].on()
sleep(5)
