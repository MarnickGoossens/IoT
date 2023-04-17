import time
import wiringpi
import sys


print("Start")
trg = 1
echo = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(echo, 0)
wiringpi.pinMode(trg, 1)

while True:
    wiringpi.digitalWrite(trg, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(trg, 0)

    while wiringpi.digitalRead(echo) == 0:
        startTime = time.time()

    while wiringpi.digitalRead(echo) == 1:
        stopTime = time.time()

    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2

    print(distance)
    time.sleep(0.5)
