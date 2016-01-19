import RPi.GPIO as GPIO
import time
import easygui
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
HowManyLed = int(input("რამდენი ნათურა გაქვთ?\t"))
Leds = []
for LedsLoop in range(HowManyLed):
    Leds.append(LedsLoop)
RedLedPin = int(input("%s ნათურის პინის ნომერი" % Leds[0]))
greenledpin = pass
whiteledpin = 15
blueledpin = 21
GPIO.setup(RedLedPin,GPIO.OUT)
GPIO.setup(greenledpin,GPIO.OUT)
GPIO.setup(whiteledpin,GPIO.OUT)
GPIO.setup(blueledpin,GPIO.OUT)

i = 1
while i == 1:
    reply = int(input("LED ნათება\n1.წითელი-ჩართვა\n2.წითელი-ციმციმი\n3.წითელი-გამორთვა\n4.მწვანე-ჩართვა\n5.მწვანე-ციმციმი\n6.მწვანე-გამორთვა\n7.მეტი\n8.გამოსვლა\nშეიყვანე ციფრი:\t"))

## წითელი
#### წითელი ჩართვა
    if reply == "1":
        GPIO.output(RedLedPin,GPIO.HIGH)
#### წითელი ციმციმი
    elif reply == "2":
        redblink = True
        while redblink == True:
            print("ციმციმი")
            replyredblink = input("1.ციმციმი\n2.ციმციმის გამორთვა\n")
            if replyredblink == "1":
                BlinkNumberRed = int(input("რამდენჯერ უნდა დაიციმციმოს?"))
                blinkpersecondred = int(input("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში "))
                timesleepred = 1 / BlinkPerSecondRed
                for x in range(BlinkNumberRed):
                    GPIO.output(RedLedPin,GPIO.HIGH)
                    time.sleep(timesleepred)
                    GPIO.output(RedLedPin,GPIO.LOW)
                    time.sleep(timesleepred)
            elif replyredblink == "2":
                redblink = False
#### წითელი გამორთვა
    elif reply == "3":
        GPIO.output(RedLedPin,GPIO.LOW)

## მწვანე
    elif reply == "მწვანე-ჩართვა":
        GPIO.output(greenledpin,GPIO.HIGH)
    elif reply == "მწვანე-ციმციმი":
        greenblink = True
        while greenblink == True:
            replygreenblink = easygui.buttonbox("ციმციმი",choices = ["ციმციმი","ციმციმის გამორთვა"])
            if replygreenblink == "ციმციმი":
                blinknumbergreen = easygui.integerbox("რამდენჯერ უნდა დაიციმციმოს?")
                blinkpersecondgreen = easygui.integerbox("რა სიჩქარით იციმციმოს? x დაციმციმება 1 წამში  ")
                timesleepgreen = 1 / blinkpersecondgreen
                for x in range(blinknumbergreen):
                    GPIO.output(greenledpin,GPIO.HIGH)
                    time.sleep(timesleepgreen)
                    GPIO.output(greenledpin,GPIO.LOW)
                    time.sleep(timesleepgreen)
            elif replygreenblink == "ციმციმის გამორთვა":
                greenblink = False
    elif reply == "მწვანე-გამორთვა":
        GPIO.output(greenledpin,GPIO.LOW)

## მენიუ მეტი
    elif reply == "მეტი":
        meti = True
        while meti == True:
            metimenu = easygui.buttonbox("დააჭირეთ ღილაკს",choices = ["ნათურის სიკაშკაშე","შემთხვევითი ნათება","მასიური ციმციმი","გამოსვლა"])

        ## ნათურის სიკაშკაშე
            if metimenu == "ნათურის სიკაშკაშე":

            ## ნათურის არჩევა სიკაშკაშე
                ledbrightnessledchoiceloop = True
                while ledbrightnessledchoiceloop == True:
                    ledchoicebrightness = easygui.buttonbox("აირჩიეთ ნათურა",choices = ["წითელი","მწვანე","თეთრი","გამოსვლა"])

                    ## წითელი ნათურის სიკაშკაშე
                    if ledchoicebrightness == "წითელი":
                        redledbrightnessloop = True
                        while redledbrightnessloop == True:
                            ledbrightnesswelcome = easygui.indexbox("წითელი ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?",choices = ["დიახ","არა"])
                            if ledbrightnesswelcome == 0:
                                redledbrightnessdutycycle = easygui.integerbox("Duty cycle",default = 50,lowerbound = 0,upperbound = 100) # change later
                                redbrightness = GPIO.PWM(RedLedPin,200)
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
                            GPIO.output(RedLedPin,GPIO.HIGH) #red
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(RedLedPin,GPIO.LOW)
                            GPIO.output(whiteledpin,GPIO.HIGH) #white
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(whiteledpin,GPIO.LOW)
                            GPIO.output(greenledpin,GPIO.HIGH) #green
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(greenledpin,GPIO.LOW)
                            GPIO.output(blueledpin,GPIO.HIGH) #blueledpin
                            time.sleep(speedofrandomblinkfloat)
                            GPIO.output(blueledpin,GPIO.LOW)
                    else:
                        randomblinkloop == False

        ## მენიუ მეტიდან გამოსვლა
            else:
                meti = False

    ## გამოსვლა
    else:
        exit = easygui.buttonbox("ნამდვიალად გსურთ გამოსვლა?",choices=["კი","არა"])
        if exit == ("კი"):
            i=2
            GPIO.cleanup()
        else:
            print("-")
            pass
