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
            for x in range(BlinkNumberLed):

                Leds[LedsNumberFunction].blink(TimeSleepLed,TimeSleepLed,BlinkNumberLed,False)

        elif ReplyLedBlink  == 2:
            LedFadeLoop = True
            while LedFadeLoop == True:
                LedFadeInput = int(input("\nგსურთ გაგრძელება?\n1.დიახ\n2.არა"))
                if LedFadeInput == 1:
                    for FadeDown in range(100):
                        LedFadeDutyCycle = 100
                        LedFade = GPIO.PWM(Leds[0], 200)
                        LedFade.start(LedFadeDutyCycle)
                        LedFadeDutyCycle -= 1

                    for FadeDown in range(100):
                        LedFade = GPIO.PWM(Leds[0], 200)
                        LedFade.start(LedFadeDutyCycle)
                        LedFadeDutyCycle += 1
                else:
                    LedFade.stop()
                    LedFadeLoop = False

        else:
            LedBlink = False
    return;

def TurnLedOffFunction (LedsNumberFunction):
    Leds[LedsNumberFunction].off()
    print("ნათურა გამოირთო!")
    return;

#####################

from gpiozero import LED
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
for LedsLoop in range(1, HowManyLed + 1):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop - 1]))
    Leds[LedsLoop] = LED(LedsInput)
print(Leds)

MenuList = ["\nLED ნათება\n","1080.მეტი\n1090.გამოსვლა\n\nშეიყვანე ციფრი:\t"]
MenuListIndex = 1
MenuListLedNumber = 1
MenuListNumberOne = 1
MenuListNumberTwo = 2
MenuListNumberThree = 3

for MenuLoop in range(HowManyLed):

    strMenuListLedNumber = str(MenuListLedNumber)
    strMenuListNumberOne = str(MenuListNumberOne)
    strMenuListNumberTwo = str(MenuListNumberTwo)
    strMenuListNumberThree = str(MenuListNumberThree)

    MenuListString = strMenuListNumberOne + ". " + strMenuListLedNumber + " ნათურა - ჩართვა\n" + strMenuListNumberTwo + ". " + strMenuListLedNumber + " ნათურა - ციმციმი\n" + strMenuListNumberThree + ". " + strMenuListLedNumber + " ნათურა - გამორთვა\n\n"
    MenuList.insert(MenuListIndex, MenuListString)

    MenuListLedNumber += 1
    MenuListIndex += 1
    MenuListNumberOne += 3
    MenuListNumberTwo += 3
    MenuListNumberThree += 3

MenuList = ''.join(MenuList)

i = 1
while i == 1:

    reply = int(input(MenuList))
    print("\n")

## პირველი ნათურა
#### პირველი ნათურა ჩართვა
    if reply == 1:
        TurnLedOnFunction(1)

#### პირველი ნათურა ციმციმი
    elif reply == 2:
        LedBlinkFunction(1)

#### პირველი ნათურა გამორთვა
    elif reply == 3:
        TurnLedOffFunction(1)
## მეორე ნათურა

#### მეორე ნათურის ჩართვა
    if reply == 4:
        TurnLedOnFunction(2)

#### მეორე ნათურის ციმციმი
    elif reply == 5:
        LedBlinkFunction(2)

#### მეორე ნათურის გამორთვა
    elif reply == 6:
        TurnLedOffFunction(2)

## მესამე ნათურა
#### მესამე ნათურის ჩართვა
    if reply == 7:
        TurnLedOnFunction(3)

#### მესამე ნათურის ციმციმი
    elif reply == 8:
        LedBlinkFunction(3)

#### მესამე ნათურის გამორთვა
    elif reply == 9:
        TurnLedOffFunction(3)

    ## გამოსვლა
    elif reply == 1090:
        exit = int(input("ნამდვიალად გსურთ გამოსვლა?\n1.კი\n2.არა\nჩაწერეთ ციფრი:\t"))
        if exit == 1:
            i=2
            GPIO.cleanup()
        else:
            print("-")

## არაფერი
    else:
        pass
