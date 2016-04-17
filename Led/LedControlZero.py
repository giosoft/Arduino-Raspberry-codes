###################

def TurnLedOnFunction(LedsNumberFunction):
    Leds[LedsNumberFunction].on()
    print("ნათურა აინთო!")

def LedBlinkFunction(LedsNumberFunction):
    LedBlink = True
    while LedBlink == True:
        print("\nციმციმი")
        ReplyLedBlink = int(input("1.უხეში ციმციმი\n2.ნაზი ციმციმი\n3.ციმციმის გამორთვა\n"))

        if ReplyLedBlink == 1:
            BlinkNumberLed = int(input("რამდენჯერ უნდა დაიციმციმოს?\t"))
            BlinkPerSecondLed = float(input("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში\t"))
            TimeSleepLed = 1 / BlinkPerSecondLed / 2
            Leds[LedsNumberFunction].blink(TimeSleepLed, TimeSleepLed, BlinkNumberLed)

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

def TurnLedOffFunction (LedsNumberFunction):
    Leds[LedsNumberFunction].off()
    print("ნათურა გამოირთო!")

#####################

from gpiozero import PWMLED
from time import sleep

########## setup ########################################################

HowManyLed = int(input("რამდენი ნათურა გაქვთ?\t"))

LedsNumber = []
for LedsNumberLoop in range (HowManyLed):
    LedsNumber.append(LedsNumberLoop + 1)
print(LedsNumber)

LedsInputList = []
Leds = {}
for LedsLoop in range(HowManyLed):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop]))
    LedsInputList.append(LedsInput)
    Leds[LedsLoop + 1] = PWMLED(LedsInput)
print(Leds)

RawLedsAndFriends = []
for LedsAndFriendsLoop in range (HowManyLed):
    RawLedsAndFriends.append(LedsNumber[LedsAndFriendsLoop])
    RawLedsAndFriends.append("-")
    RawLedsAndFriends.append(LedsInputList[LedsAndFriendsLoop])
RawLedsAndFriends.append("0-გამოსვლა")
print(RawLedsAndFriends)
LedsAndFriends = ''.join(RawLedsAndFriends)
print(LedsAndFriends)

RawLedsAndFriendsBlinkEdition = RawLedsAndFriends
RawLedsAndFriendsBlinkEdition.append("100-რამოდენიმეს ერთად არჩევა")
print(RawLedsAndFriendsBlinkEdition)
LedsAndFriendsBlinkEdition = ''.join(RawLedsAndFriendsBlinkEdition)
print(LedsAndFriendsBlinkEdition)

########## setup ########################################################

Menu = "\nLED ნათურის კონტროლი\n\n1.ანთება\n2.ციმციმი\n3.ჩაქრობა\n0.გამოსვლა\n\nშეიყვანე ციფრი:\t"

i = 1
while i == 1:

    reply = int(input(Menu))
    print("\n")

#### ანთება
    if reply == 1:
        LedOnLoop = True
        while LedOnLoop == True:
            LedOnInput = int(input(LedsAndFriends))
            if LedOnInput == 0:
                LedOnLoop = False

            else:
                TurnLedOnFunction(LedOnInput)

#### ციმციმი
    elif reply == 2:
        LedBlinkLoop = True
        while LedBlinkLoop == True:
            LedBlinkInput = int(input(LedsAndFriendsBlinkEdition))
            if LedBlinkInput == 100:
                print("\nრამოდენიმეს ერთად არჩევა\n")
                LedBlinkMultiInput = int(input(LedsAndFriends))


            elif LedBlinkInput == 0:
                LedBlinkLoop = False

            else:
                LedBlinkFunction(LedBlinkInput)

#### ჩაქრობა
    elif reply == 3:
        LedOffLoop = True
        while LedOffLoop == True:
            LedOffInput = int(input(LedsAndFriends))
            if LedOffInput == 0:
                LedOffLoop = False

            else:
                TurnLedOffFunction(LedOffInput)

## გამოსვლა
    elif reply == 0:
        exit = int(input("ნამდვიალად გსურთ გამოსვლა?\n1.კი\n2.არა\nჩაწერეთ ციფრი:\t"))
        if exit == 1:
            i = 2
        else:
            pass

## შეცდომა
    else:
        print("თქვენი შეყვანილი ციფრი არასწორია.\nგთხოვთ სცადოთ თავიდან!\n")
