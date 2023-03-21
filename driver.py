import time
import wiringpi
import sys


def setup():
    print("Start")
    pin = 2
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(pin, 1)


def blink(pin):
    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)


def main():
    for _ in range(0, 10):
        blink(pin)


setup()
main()

print("Done")
