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

def LedBasicControl(LedsNumber,LedPin):
#### ჩართვა
    if reply  == 1:
        GPIO.output(Leds[LedsNumber - 1],GPIO.HIGH)
        print("%s ნათურა აინთო", % LedsNumber)
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
                    GPIO.output(Leds[LedsNumber - 1],GPIO.HIGH)
                    time.sleep(TimeSleep)
                    GPIO.output(Leds[LedsNumber - 1],GPIO.LOW)
                    time.sleep(TimeSleep)
            else:
                blink = False
#### გამორთვა
    elif reply == 3:
        GPIO.output(Leds[LedsNumber - 1],GPIO.LOW)

####
i = 1
while i == 1:
    reply = int(input("LED ნათება\n1.First Led-ჩართვა\n2.First Led-ციმციმი\n3.First Led-გამორთვა\n4.მწვანე-ჩართვა\n5.მწვანე-ციმციმი\n6.მწვანე-გამორთვა\n7.მეტი\n8.გამოსვლა\nშეიყვანე ციფრი:\t"))
    print("\n")
####
    LedBasicControl(LedsNumber[0],Leds[0])
    LedBasicControl(LedsNumber[1],Leds[1])
    ## გამოსვლა
    else:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass
