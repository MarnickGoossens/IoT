import wiringpi
import time

# setup
counter = 1
buttonState = 0
lastButtonState = 0
buttonPin = 1
ledpin = 15
wiringpi.wiringPiSetup()
wiringpi.pinMode(buttonPin, 0)
wiringpi.pinMode(ledpin, 1)

try:
    while True:
        buttonState = wiringpi.digitalRead(buttonPin)
        if buttonState != lastButtonState:
            if buttonState == True:
                counter += 1
        else:
            time.sleep(0.05)
        lastButtonState = buttonState

        if counter % 2 == 0:
            wiringpi.digitalWrite(ledpin, 1)
        else:
            wiringpi.digitalWrite(ledpin, 0)
except KeyboardInterrupt:
    wiringpi.digitalWrite(ledpin, 0)
    print("\nDone")
