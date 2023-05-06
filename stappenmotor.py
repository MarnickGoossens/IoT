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
moterCoil1 = 3
moterCoil2 = 4
moterCoil3 = 6
moterCoil4 = 8
wiringpi.wiringPiSetup()
wiringpi.pinMode(moterCoil1, 1)
wiringpi.pinMode(moterCoil2, 1)
wiringpi.pinMode(moterCoil3, 1)
wiringpi.pinMode(moterCoil4, 1)


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
