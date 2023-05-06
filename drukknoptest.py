import wiringpi
import time

# setup
buttonPin = 0
wiringpi.wiringPiSetup()
wiringpi.pinMode(buttonPin, 0)

while True:
    print(wiringpi.digitalRead(buttonPin))
    time.sleep(1)
