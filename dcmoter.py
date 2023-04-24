import time
import wiringpi


print("Start")
pin2 = 2
pin7 = 7
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin7, 1)


wiringpi.digitalWrite(pin2, 0)
wiringpi.digitalWrite(pin7, 0)

while True:
    wiringpi.digitalWrite(pin7, 1)
    wiringpi.digitalWrite(pin2, 1)
    time.sleep(1)
    wiringpi.digitalWrite(pin2, 0)
    wiringpi.digitalWrite(pin7, 0)
    time.sleep(1)
