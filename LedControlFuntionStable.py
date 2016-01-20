#######################################################
#### Functions ########################################
#######################################################

def LedBasicControl(LedsNumberFunction):
#### ჩართვა
    if reply  == 1:
        GPIO.output(Leds[LedsNumberFunction - 1],GPIO.HIGH)
        print("%s ნათურა აინთო" % LedsNumberFunction)
#### ციმციმი
    elif reply == 2:
        blink = True
        while blink == True:
            print("\nციმციმი")
            replyblink = int(input("1.უხეში ციმციმი\n2.ნაზი ციმციმი\n3.ციმციმის გამორთვა\n"))
            if replyblink == 1:
                BlinkNumber = int(input("რამდენჯერ უნდა დაიციმციმოს?\t"))
                BlinkPerSecond = float(input("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში\t"))
                TimeSleep = 1 / BlinkPerSecond
                for x in range(BlinkNumberRed):
                    GPIO.output(Leds[LedsNumberFunction - 1],GPIO.HIGH)
                    time.sleep(TimeSleep)
                    GPIO.output(Leds[LedsNumberFunction - 1],GPIO.LOW)
                    time.sleep(TimeSleep)
            else:
                blink = False
#### გამორთვა
    elif reply == 3:
        GPIO.output(Leds[LedsNumberFunction - 1],GPIO.LOW)
    return;

#######################################################
#### THE END ##########################################
#######################################################

import RPi.GPIO as GPIO
import time
import easygui
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

i = 1
while i == 1:
    reply = int(input("LED ნათება\n\t1.First Led - ჩართვა\n\t2. Led-ციმციმი\n\t3.First Led - გამორთვა\n\t4.მეტი\n\t5.გამოსვლა\n\tშეიყვანე ციფრი:\n\t"))
    print("\n")

    LedBasicControl(LedsNumber[0],Leds[0])

## გამოსვლა
    if reply == 5:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass
