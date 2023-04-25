import wiringpi
import time

# setup
counter = 1
buttonState = 0
lastButtonState = 0
buttonPin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(buttonPin, 0)
wiringpi.pinMode(3, 1)

wiringpi.digitalWrite(3, 0)
while True:
    buttonState = wiringpi.digitalRead(buttonPin)
    if buttonState != lastButtonState:
        if buttonState == True:
            counter += 1
    else:
        time.sleep(0.05)
    lastButtonState = buttonState

    if counter % 2 == 0:
        wiringpi.digitalWrite(3, 1)
    else:
        wiringpi.digitalWrite(3, 0)
