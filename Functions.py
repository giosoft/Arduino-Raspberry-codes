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
        else:
            LedBlink = False

def TurnLedOffFunction (LedsNumberFunction):
    GPIO.output(Leds[0],GPIO.LOW)
    print("ნათურა გამოირთო!")
