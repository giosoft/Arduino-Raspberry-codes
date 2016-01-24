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
                time.sleep(TimeSleepLed)

                GPIO.output(Leds [LedsNumberFunction - 1], GPIO.LOW)
                time.sleep(TimeSleepLed)

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
