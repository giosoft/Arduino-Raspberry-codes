from gpiozero import LED
LedName = {}
LedName[1] = LED(14)
print(LedName)
LedName[1].on()
