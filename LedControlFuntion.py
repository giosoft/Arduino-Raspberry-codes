import RPi.GPIO as GPIO
import time
import easygui
from LedFunction import LedBasicControl
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

HowManyLed = int(input("რამდენი ნათურა გაქვთ?\t"))
LedsNumber = []
for LedsNumberLoop in range (HowManyLed):
    LedsNumber.append(LedsNumberLoop + 1)
Leds = []
for LedsLoop in range(1, HowManyLed + 1):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop - 1]))
    Leds.append(LedsInput)
    GPIO.setup(Leds[LedsLoop - 1],GPIO.OUT)
x = 1
i = 1
while i == 1:
    reply = int(input("LED ნათება\n1.First Led-ჩართვა\n2.First Led-ციმციმი\n3.First Led-გამორთვა\n4.მწვანე-ჩართვა\n5.მწვანე-ციმციმი\n6.მწვანე-გამორთვა\n7.მეტი\n8.გამოსვლა\nშეიყვანე ციფრი:\t"))
    print("\n")
####
    Ham = True
    if Ham == True:
        LedBasicControl(LedsNumber[0],Leds[0])
    ## გამოსვლა
    else:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass
