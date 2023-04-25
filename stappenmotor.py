import time
import wiringpi
import sys


def reset():
    wiringpi.digitalWrite(1, 0)
    wiringpi.digitalWrite(4, 0)
    wiringpi.digitalWrite(6, 0)
    wiringpi.digitalWrite(8, 0)


def full_step():
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)


def wave_drive():
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 1)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 1)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 0)
    wiringpi.digitalWrite(coil2, 1)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)
    wiringpi.digitalWrite(coil1, 1)
    wiringpi.digitalWrite(coil2, 0)
    wiringpi.digitalWrite(coil3, 0)
    wiringpi.digitalWrite(coil4, 0)
    time.sleep(stopTijd)


# setup
stopTijd = 0.01
coil1 = 3
coil2 = 4
coil3 = 6
coil4 = 8
wiringpi.wiringPiSetup()
wiringpi.pinMode(coil1, 1)
wiringpi.pinMode(coil2, 1)
wiringpi.pinMode(coil3, 1)
wiringpi.pinMode(coil4, 1)


# loop
print("start")
reset()
try:
    while True:
        # wave_drive()
        full_step()
except KeyboardInterrupt:
    reset()
    print("\ndone")
