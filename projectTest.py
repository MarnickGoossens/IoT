from wiringpi import (
    wiringPiSetup,
    wiringPiSPISetupMode,
    pinMode,
    digitalWrite,
    digitalRead,
)
from datetime import datetime
from time import sleep, time
from ch7_ClassLCD import LCD
import spidev
import threading


# Functies
def ultrasone(trg, echo, startTime, stopTime):
    digitalWrite(trg, 1)
    sleep(0.00001)
    digitalWrite(trg, 0)

    while digitalRead(echo) == 0:
        startTime = time()

    while digitalRead(echo) == 1:
        stopTime = time()

    tijd = stopTime - startTime
    afstand = round(tijd * 17000)
    return afstand


def moterReset(coil1, coil2, coil3, coil4):
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 0)


def full_step(coil1, coil2, coil3, coil4):
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 1)
    digitalWrite(coil4, 1)
    sleep(0.01)
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 1)
    digitalWrite(coil3, 1)
    digitalWrite(coil4, 0)
    sleep(0.01)
    digitalWrite(coil1, 1)
    digitalWrite(coil2, 1)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 0)
    sleep(0.01)
    digitalWrite(coil1, 1)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 1)
    sleep(0.01)
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 1)
    digitalWrite(coil4, 1)
    sleep(0.01)
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 1)
    digitalWrite(coil3, 1)
    digitalWrite(coil4, 0)
    sleep(0.01)
    digitalWrite(coil1, 1)
    digitalWrite(coil2, 1)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 0)
    sleep(0.01)
    digitalWrite(coil1, 1)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 1)
    sleep(0.01)


def ActivateLCD():
    digitalWrite(pinCsLCD, 0)
    sleep(0.000005)


def updateLCD(trapped, trapCounter):
    lcd1.clear()
    lcd1.go_to_xy(0, 0)
    lcd1.put_string(datetime.now().strftime("%d/%m/%Y"))
    lcd1.go_to_xy(0, 10)
    lcd1.put_string(datetime.now().strftime("%H:%M:%S"))
    lcd1.go_to_xy(0, 20)
    if not trapped:
        lcd1.put_string(f"armed")
    else:
        lcd1.put_string(f"triggered")
    lcd1.go_to_xy(0, 30)
    lcd1.put_string(f"trapped: {trapCounter}")
    lcd1.refresh()


def DeactivateLCD():
    digitalWrite(pinCsLCD, 1)  # Deactived LCD using CS
    sleep(0.000005)


def main(trapped, timeTrapped, trapCounter):
    try:
        while True:
            while not trapped:
                if digitalRead(buttonPin2) == True:
                    full_step(coil1, coil2, coil3, coil4)

                ultrasoneAfstand = ultrasone(
                    trg, echo, ultrasoneStartTime, ultrasoneStopTime
                )
                if ultrasoneAfstand < 10:
                    trapped = True
                    trapCounter += 1
                    timeTrapped = time()
                    digitalWrite(ledpin, True)

            while timeTrapped + 5 > time():
                full_step(coil1, coil2, coil3, coil4)

            if digitalRead(buttonPin1) == True:
                trapped = False
                moterReset(coil1, coil2, coil3, coil4)
                digitalWrite(ledpin, False)

    except KeyboardInterrupt:
        lcd1.clear()
        lcd1.refresh()
        DeactivateLCD()


# Variabele
ultrasoneStartTime = 0
ultrasoneStopTime = 0
trapped = False
timeTrapped = 0
trapCounter = 0

# Pinnen
buttonPin1 = 1
buttonPin2 = 0
ledpin = 15
trg = 5
echo = 7
coil1 = 3
coil2 = 4
coil3 = 6
coil4 = 8
pinOutLCD = {
    "SCLK": 14,
    "DIN": 11,
    "DC": 9,
    "CS": 15,  # We will not connect this pin! --> we use w13
    "RST": 10,
    "LED": 6,  # backlight
}
pinCsLCD = 13

# Setup
wiringPiSetup()
wiringPiSPISetupMode(1, 0, 400000, 0)  # (channel, port, speed, mode)
pinMode(buttonPin1, 0)
pinMode(buttonPin2, 0)
pinMode(ledpin, 1)
pinMode(trg, 1)
pinMode(echo, 0)
pinMode(coil1, 1)
pinMode(coil2, 1)
pinMode(coil3, 1)
pinMode(coil4, 1)
pinMode(pinCsLCD, 1)
ActivateLCD()
lcd1 = LCD(pinOutLCD)
lcd1.clear()


t1 = threading.Thread(target=updateLCD, args=(trapped, trapCounter))
t2 = threading.Thread(target=main, args=(trapped, timeTrapped, trapCounter))

t2.start()
t1.start()
