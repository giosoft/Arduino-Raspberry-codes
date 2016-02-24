def LedBrightnessFunction(LedsNumberFunction):
    LedBrightnessLoop = True
    while LedBrightnessLoop == True:

        if LedBrightnessWelcome == 1:
            Leds[LedsNumberFunction].on()
            LedBrightnessDutyCycle = int(input("სიკაშკაშის დონე (1-100):\t")) # change later
            Leds[LedsNumberFunction].value = LedBrightnessDutyCycle / 100

            LedBrightnessWelcome = int(input(("ნათურის სიკაშკაშის კონტროლი\nგსურთ გაგრძელება?\n1.დიახ\t2.არა"))

        elif == 2:
            LedBrightnessLoop = False
            
        else:
            print("ციფრი არასწორად არის შეყვანილი, გთხოვთ სცადოთ თავიდან!")
