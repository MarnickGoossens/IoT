import time
import wiringpi
import sys


trg = 5
echo = 7
startTime = 0
stopTime = 0
ultrasone_tijd = 0
ultrasone_afstand = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(trg, 1)
wiringpi.pinMode(echo, 0)

try:
    while True:
        wiringpi.digitalWrite(trg, 0)
        time.sleep(0.2)
        wiringpi.digitalWrite(trg, 1)
        time.sleep(0.00001)
        wiringpi.digitalWrite(trg, 0)

        while wiringpi.digitalRead(echo) == 0:
            startTime = time.time()

        while wiringpi.digitalRead(echo) == 1:
            stopTime = time.time()

        ultrasone_tijd = stopTime - startTime
        ultrasone_afstand = round((ultrasone_tijd * 17000), 2)
        print(ultrasone_afstand)
        time.sleep(1)

except KeyboardInterrupt:
    print("Done")
