###################

def TurnLedOnFunction(LedsNumberFunction):
    GPIO.output(Leds [LedsNumberFunction - 1],GPIO.HIGH)
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
            TimeSleepLed = 1 / BlinkPerSecondLed
            for x in range(BlinkNumberLed):

                GPIO.output(Leds [LedsNumberFunction - 1], GPIO.HIGH)
                sleep(TimeSleepLed)

                GPIO.output(Leds [LedsNumberFunction - 1], GPIO.LOW)
                sleep(TimeSleepLed)

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
    GPIO.output(Leds[0],GPIO.LOW)
    print("ნათურა გამოირთო!")
    return;

#####################

from gpiozero import LED
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

Leds = []
for LedsLoop in range(1, HowManyLed + 1):
    LedsInput = int(input("ჩაწერეთ %s ნათურის პინის ნომერი:\t" % LedsNumber[LedsLoop - 1]))
    Leds.append(LedsInput)
    GPIO.setup(Leds[LedsLoop - 1],GPIO.OUT)
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

## მენიუ მეტი
    elif reply == 1080:
        meti = True
        while meti == True:
            metimenu = easygui.buttonbox("დააჭირეთ ღილაკს",choices = ["ნათურის სიკაშკაშე","შემთხვევითი ნათება","მასიური ციმციმი","გამოსვლა"])

        ## ნათურის სიკაშკაშე
            if metimenu == "ნათურის სიკაშკაშე":

            ## ნათურის არჩევა სიკაშკაშე
                ledbrightnessledchoiceloop = True
                while ledbrightnessledchoiceloop == True:
                    ledchoicebrightness = easygui.buttonbox("აირჩიეთ ნათურა",choices = ["First Led","მწვანე","თეთრი","გამოსვლა"])

                    ## First Led ნათურის სიკაშკაშე
                    if ledchoicebrightness == "First Led":
                        redledbrightnessloop = True
                        while redledbrightnessloop == True:
                            ledbrightnesswelcome = easygui.indexbox("First Led ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?",choices = ["დიახ","არა"])
                            if ledbrightnesswelcome == 0:
                                redledbrightnessdutycycle = easygui.integerbox("Duty cycle",default = 50,lowerbound = 0,upperbound = 100) # change later
                                redbrightness = GPIO.PWM(Leds[0], 200)
                                redbrightness.start(redledbrightnessdutycycle)
                            else:
                                redbrightness.stop()
                                ledbrightnessloop = False
                                ledbrightnessledchoiceloop = False
                    if ledchoicebrightness == "მწვანე":
                        greenledbrightnessloop = True
                        while greenledbrightnessloop == True:
                            greenledbrightnesswelcome = easygui.indexbox("მწვანე ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?",choices = ["დიახ","არა"])
                            if greenledbrightnesswelcome == 0:
                                greenledbrightnessdutycycle = easygui.integerbox("აირჩიეთ სიკაშკაშის დონე\n0 - min // 100 - max",default = 50,lowerbound = 0,upperbound = 100) # change later
                                greenbrightness = GPIO.PWM(greenledpin,200)
                                greenbrightness.start(greenledbrightnessdutycycle)
                            else:
                                greenbrightness.stop()
                                greenledbrightnessloop = False
                                GPIO.cleanup()
                    else:
                        ledbrightnessledchoiceloop = False
                        GPIO.cleanup()

            ## შემთხვევითი ნათება
            elif metimenu == "შემთხვევითი ნათება (მასიური)":
                pass

            ## მასიური ციმციმი
            elif metimenu == "მასიური ციმციმი":
                randomblinkloop = True
                while randomblinkloop == True:
                    welcomerandomblinkloop = easygui.buttonbox("გსურთ გაგრძელება?", choices =  ["კი","არა"])
                    if welcomerandomblinkloop == "კი":
                        numberofrandomblink = easygui.integerbox("რაოდენობა: ",default = 5,lowerbound = 0,upperbound = 50)
                        speedofrandomblinkstring = easygui.enterbox("სიჩქარე")
                        speedofrandomblinkfloat = float(speedofrandomblinkstring)
                        for randomblinkforloop in range(numberofrandomblink):

                            GPIO.output(Leds[0],GPIO.HIGH) #red
                            sleep(speedofrandomblinkfloat)
                            GPIO.output(Leds[0],GPIO.LOW)

                            GPIO.output(whiteledpin,GPIO.HIGH) #white
                            sleep(speedofrandomblinkfloat)
                            GPIO.output(whiteledpin,GPIO.LOW)

                            GPIO.output(greenledpin,GPIO.HIGH) #green
                            sleep(speedofrandomblinkfloat)
                            GPIO.output(greenledpin,GPIO.LOW)

                            GPIO.output(blueledpin,GPIO.HIGH) #blueledpin
                            sleep(speedofrandomblinkfloat)
                            GPIO.output(blueledpin,GPIO.LOW)
                    else:
                        randomblinkloop == False

        ## მენიუ მეტიდან გამოსვლა
            else:
                meti = False

    ## გამოსვლა
    elif reply == 1090:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass

## არაფერი
    else:
        pass
