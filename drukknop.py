import wiringpi
import time

# setup
counter = 1
buttonState1 = 0
lastButtonState1 = 0
buttonPin1 = 1
ledpin = 15
wiringpi.wiringPiSetup()
wiringpi.pinMode(buttonPin1, 0)
wiringpi.pinMode(ledpin, 1)

try:
    while True:
        buttonState1 = wiringpi.digitalRead(buttonPin1)
        if buttonState1 != lastButtonState1:
            if buttonState1 == True:
                counter += 1
        lastButtonState1 = buttonState1

        if counter % 2 == 0:
            wiringpi.digitalWrite(ledpin, 1)
        else:
            wiringpi.digitalWrite(ledpin, 0)
except KeyboardInterrupt:
    wiringpi.digitalWrite(ledpin, 0)
    print("\nDone")
