import time
import wiringpi
import sys


def blink(pin):
    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)


print("Start")
pin = 8
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)

for _ in range(10):
    blink(pin)

print("Done")
