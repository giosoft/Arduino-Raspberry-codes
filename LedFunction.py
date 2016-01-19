def LedBasicControl(LedsNumber,LedPin):
    global LedsNumber
    global Leds
    print (reply)
#### ჩართვა
    if reply  == 1:
        GPIO.output(Leds[LedsNumber - 1],GPIO.HIGH)
        print("%s ნათურა აინთო" % LedsNumber)
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
    return;
