from gpiozero import LED
LedName = {}
LedName[1] = LED(14)
print(LedName[1])
LedName[1].on()
