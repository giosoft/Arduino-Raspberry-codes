###################

def TurnLedOnFunction(LedsNumberFunction):
    Leds[LedsNumberFunction].on()
    print("ნათურა აინთო!")
    return;

def LedBlinkFunction(LedsNumberFunction):
    LedBlink = True
    while LedBlink == True:
        print("\nციმციმი")
        ReplyLedBlink = int(input("1.უხეში ციმციმი\n2.ნაზი ციმციმი\n3.ციმციმის გამორთვა\n"))

        if ReplyLedBlink == 1:
            BlinkNumberLed = int(input("რამდენჯერ უნდა დაიციმციმოს?\t"))
            BlinkPerSecondLed = float(input("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში\t"))
            TimeSleepLed = 1 / BlinkPerSecondLed / 2

            Leds[LedsNumberFunction].blink(TimeSleepLed,TimeSleepLed,BlinkNumberLed)

        elif ReplyLedBlink  == 2:
            LedFadeNumber = int(input("რამდენჯერ გსურთ?\t"))
            LedFadePause = float(input("სიჩქარე\t"))
            for i in range(LedFadeNumber):
                Leds[LedsNumberFunction].off()
                for i in range(101):
                    Leds[LedsNumberFunction].value = i / 100
                    sleep(LedFadePause)
                Leds[LedsNumberFunction].on()
                for i in range(101):
                    Leds[LedsNumberFunction].value = (100 - i) / 100
                    sleep(LedFadePause)

        else:
            LedBlink = False
    return;

def TurnLedOffFunction (LedsNumberFunction):
    Leds[LedsNumberFunction].off()
    print("ნათურა გამოირთო!")
    return;

#####################

from gpiozero import PWMLED
import RPi.GPIO as GPIO
from time import sleep
import easygui

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

HowManyLed = int(input("რამდენი ნათურა გაქვთ?\t"))

LedsNumber = []
for LedsNumberLoop in range (HowManyLed):
    LedsNumber.append(LedsNumberLoop + 1)
print(LedsNumber)

Leds = {}
for LedsLoop in range(HowManyLed):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop]))
    Leds[LedsLoop + 1] = PWMLED(LedsInput)
print(Leds)

Menu = "\nLED ნათურის კონტროლი\n\n1.ანთება\n2.ციმციმი\n3.ჩაქრობა\n0.გამოსვლა\n\nშეიყვანე ციფრი:\t"

i = 1
while i == 1:

    reply = int(input(Menu))
    print("\n")

## პირველი ნათურა
#### პირველი ნათურა ჩართვა
    if reply == 1:
        LedOnLoop = True
            while LedOnLoop == True:


#### პირველი ნათურა ციმციმი
    elif reply == 2:

#### პირველი ნათურა გამორთვა
    elif reply == 3:


## გამოსვლა
    elif reply == 1090:
        exit = int(input("ნამდვიალად გსურთ გამოსვლა?\n1.კი\n2.არა\nჩაწერეთ ციფრი:\t"))
        if exit == 1:
            i=2
            GPIO.cleanup()
        else:
            pass

## არაფერი
    else:
        print("თქვენი შეყვანილი ციფრი არასწორია.\nგთხოვთ სცადოთ თავიდან!\n")
