// constants won't change. They're used here to
// set pin numbers:
const int RedLedPin =  5;
const int GreenLedPin = 0;
const int BlueLedPin = 4;
const int buttonPin1 = 6;
const int buttonPin2 = 4;
const int buttonPin3 = 2;

// variables will change:
int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int index = 0;
int buttonResponse = clickCheck(300);
int ModeIndex = 0;

char ModeList[5] = {'Basic', 'Blink', 'Fade', 'photoColor', 'photoBlink'};

void setup() {
  // initialize the LED pins as an output:
  pinMode(RedLedPin, OUTPUT);
  pinMode(GreenLedPin, OUTPUT);
  pinMode(BlueLedPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
}

void loop() {
  Modes(ModeList[ModeIndex]);

}

void Modes(char Mode) {
  // Basic
  if(Mode == 'Basic'){
    char MIXORLIGHT = 'MIX';

    while(buttonResponse != 2){ // not sure
      colorPallete(MIXORLIGHT, index);

      if(buttonResponse == 1){
        index = index + 1;
      }
      else if(buttonResponse == 3){
        if(index > 0){
          index = index - 1;
        }
      }
      else if(buttonResponse == 7){
        if(MIXORLIGHT == 'MIX'){
          MIXORLIGHT = 'MIXLIGHT';
        }
        else if(MIXORLIGHT == 'MIXLIGHT'){
          MIXORLIGHT = 'MIX';
        }
      }
    }
  }
  // Blink
  else if(Mode == 'Blink'){

  }
  // Fade
  else if(Mode == 'Fade'){

  }
  // PhotoColor
  else if(Mode == "photoColor"){

  }
  // PhotoBlick
  else if(Mode == "photoBlink"){

  }
}

void colorPallete(char color, int colorIndex) {
  // MIX of colors for Basic, Blink, Fade
  if(color == 'MIX'){
    if(colorIndex == 0){
      rgb(22, 160, 133);
    }
    else if(colorIndex == 1){
      rgb(39, 174, 96);
    }
    else if(colorIndex == 2){
      rgb(41, 128, 185);
    }
    else if(colorIndex == 3){
      rgb(142, 68, 173);
    }
    else if(colorIndex == 4){
      rgb(44, 62, 80);
    }
    else if(colorIndex == 5){
      rgb(243, 156, 18);
    }
    else if(colorIndex == 6){
      rgb(211, 84, 0);
    }
    else if(colorIndex == 7){
      rgb(192, 57, 43);
    }
    else if(colorIndex == 8){
      rgb(189, 195, 199);
    }
    else if(colorIndex = 9){
      rgb(127, 140, 141);
    }
  }
  // Light MIX
  else if(color == 'MIXLIGHT'){
    if(colorIndex == 0){
      rgb(26, 188, 156);
    }
    else if(colorIndex == 1){
      rgb(46, 204, 113);
    }
    else if(colorIndex == 2){
      rgb(52, 152, 219);
    }
    else if(colorIndex == 3){
      rgb(155, 89, 182);
    }
    else if(colorIndex == 4){
      rgb(52, 73, 94);
    }
    else if(colorIndex == 5){
      rgb(241, 196, 15);
    }
    else if(colorIndex == 6){
      rgb(230, 126, 34);
    }
    else if(colorIndex == 7){
      rgb(231, 76, 60);
    }
    else if(colorIndex == 8){
      rgb(236, 240, 241);
    }
    else if(colorIndex == 9){
      rgb(149, 165, 166);
    }
  }
  // RED color Shades
  else if(color == 'Red'){
    if(colorIndex == 0){
      rgb(252, 180, 184);
    }
    else if(colorIndex == 1){
      rgb(251, 143, 148);
    }
    else if(colorIndex == 2){
      rgb(249, 106, 113);
    }
    else if(colorIndex == 3){
      rgb(248, 69, 77);
    }
    else if(colorIndex == 4){
      rgb(248, 69, 77);
    }
    else if(colorIndex == 5){
      rgb(248, 51, 60);
    }
    else if(colorIndex == 6){
      rgb(226, 47, 55);
    }
    else if(colorIndex == 7){
      rgb(181, 38, 44);
    }
    else if(colorIndex == 8){
      rgb(136, 28, 33);
    }
  }
}

void rgb(int red, int green, int blue) {
  red = 255 - red;
  green = 255 - green;
  blue = 255 - blue;

  analogWrite(RedLedPin, red);
  analogWrite(GreenLedPin, green);
  analogWrite(BlueLedPin, blue);
}

void clickCheck(int delayTime) {
  buttonState1 = digitalRead(buttonPin1);
  delay(delayTime);
  buttonState2 = digitalRead(buttonPin2);
  delay(delayTime);
  buttonState3 = digitalRead(buttonPin3);

  if(buttonState1 == LOW && buttonState2 == LOW && buttonState3 == LOW){
    return 0;
  }
  else if(buttonState1 == HIGH && buttonState2 == LOW && buttonState3 == LOW){
    return 1;
  }
  else if(buttonState1 == LOW && buttonState2 == HIGH && buttonState3 == LOW){
    return 2;
  }
  else if(buttonState1 == LOW && buttonState2 == LOW && buttonState3 == HIGH){
    return 3;
  }
  else if(buttonState1 == HIGH && buttonState2 == HIGH && buttonState3 == LOW){
    return 4;
  }
  else if(buttonState1 == LOW && buttonState2 == HIGH && buttonState3 == HIGH){
    return 5;
  }
  else if(buttonState1 == HIGH && buttonState2 == LOW && buttonState3 == HIGH){
    return 6;
  }
  else if(buttonState1 == HIGH && buttonState2 == HIGH && buttonState3 == HIGH){
    return 7;
  }
}
