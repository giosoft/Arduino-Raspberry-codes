while True:
    LedFadeInput = int(input("\nგსურთ გაგრძელება?\n1.დიახ\n2.არა"))
    if LedFadeInput == 1:
        for FadeDown in range(100):
            LedFadeDutyCycle = 100
            LedFade = GPIO.PWM(Leds[0], 200)
            LedFade.start(redledbrightnessdutycycle)
            LedFadeDutyCycle -= 1

        for FadeDown in range(100):
            LedFade = GPIO.PWM(Leds[0], 200)
            LedFade.start(redledbrightnessdutycycle)
            LedFadeDutyCycle += 1
    else:
        LedFade.stop()
        LedFadeLoop = False
