# Importeren van de nodige bibliotheken
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
import json
import requests
import spidev


# Functies
# Geeft de afstand tot een object door de tijd te meten van de echo pin die hoog en laag gaat
def ultrasone(trg, echo, startTime, stopTime):
    # Pulse sturen op de trg pin
    digitalWrite(trg, 1)
    sleep(0.00001)
    digitalWrite(trg, 0)

    # Als echo pin laag gaat krijgen we de start tijd
    while digitalRead(echo) == 0:
        startTime = time()

    # Als echo pin hoog gaat krijgen we de stop tijd
    while digitalRead(echo) == 1:
        stopTime = time()

    # We kunnen nu de tijd dat de echo pin laag is geweest berekenen door de tijden van elkaar af te trekken
    tijd = stopTime - startTime
    # Om de afstand te berekenen moeten we deze tijd vermenigvuldigen met 17000
    afstand = round(tijd * 17000)
    return afstand


# Zet alle motor coils op 0
def moterReset(coil1, coil2, coil3, coil4):
    digitalWrite(coil1, 0)
    digitalWrite(coil2, 0)
    digitalWrite(coil3, 0)
    digitalWrite(coil4, 0)


# Door de coils aan te sturen op de juiste manier krijgen we een krachtig koppel
# en gaat de stappen motor draaien
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


# Het lcd activeren via de CS pin
def ActivateLCD():
    digitalWrite(pinCsLCD, 0)
    sleep(0.000005)


# De waardes op het lcd printen
def updateLCD():
    ActivateLCD()
    lcd1.clear()  # Scherm leegmaken
    # Op locatie 0,0 de datum printen
    lcd1.go_to_xy(0, 0)
    lcd1.put_string(datetime.now().strftime("%d/%m/%Y"))
    # Op locatie 0,10 de tijd printen
    lcd1.go_to_xy(0, 10)
    lcd1.put_string(datetime.now().strftime("%H:%M"))
    # Op locatie 0,20 de status van de trapp printen
    lcd1.go_to_xy(0, 20)
    if not trapped:
        lcd1.put_string(f"armed")
    else:
        lcd1.put_string(f"triggered")
    # Op locatie 0,30 het aantal keer dat de trapp is afgegaan printen
    lcd1.go_to_xy(0, 30)
    lcd1.put_string(f"trapped: {trapCounter}")
    # Het scherm refreshen zodat alles op het scherm getoont word
    lcd1.refresh()
    DeactivateLCD()


# Het lcd deactiveren via de CS pin
def DeactivateLCD():
    digitalWrite(pinCsLCD, 1)  # Deactived LCD using CS
    sleep(0.000005)


# De data van de muizenval uploaden naar ubeac via json data
def uploadData(url, uid, trapped, trapCounter):
    if trapped:
        data = {
            "id": uid,
            "sensors": [
                {"id": "trapCounter", "data": trapCounter},
                {"id": "trapStatus", "data": 2},
            ],
        }
    else:
        data = {
            "id": uid,
            "sensors": [
                {"id": "trapStatus", "data": 1},
            ],
        }
    r = requests.post(url, verify=False, json=data)


# Variabele toekennen
ultrasoneStartTime = 0
ultrasoneStopTime = 0
trapped = False
timeTrapped = 0
trapCounter = 0
url = "http://marnick.hub.ubeac.io/iotmarnick"
uid = "iotmarnick"

# Pinnen configureren
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


# wiring pi initialiseren en de pinnen als input of output configureren
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


# De try/except zodat programma goed word afgesloten
try:
    # Een oneindige loop
    while True:
        updateLCD()  # Update het scherm
        # Als de trapped niet geactiveerd is
        while not trapped:
            updateLCD()  # Update het scherm
            # Check de knop voor manuele bediening van de deur
            while digitalRead(buttonPin2) == True:
                full_step(coil1, coil2, coil3, coil4)

            # Neem de afstand van de ultrasone
            ultrasoneAfstand = ultrasone(
                trg, echo, ultrasoneStartTime, ultrasoneStopTime
            )
            # Als de afstand onder de 10 cm is: upload data, laat de led branden en pas je juiste variabele aan
            if ultrasoneAfstand < 10:
                trapped = True
                trapCounter += 1
                timeTrapped = time()
                uploadData(url, uid, trapped, trapCounter)
                digitalWrite(ledpin, True)

        # Als de ultrasone iets gezien heeft binnen de 10 cm gaat de het motortje voor de deur te sluiten 5 seconden draaien
        while timeTrapped + 5 > time():
            full_step(coil1, coil2, coil3, coil4)

        # De reset knop die dient om het ledje uit te schakelen en de trap terug te activeren
        if digitalRead(buttonPin1) == True:
            trapped = False
            uploadData(url, uid, trapped, trapCounter)
            moterReset(coil1, coil2, coil3, coil4)
            digitalWrite(ledpin, False)

except KeyboardInterrupt:
    lcd1.clear()
    lcd1.refresh()
    DeactivateLCD()
    digitalWrite(ledpin, False)
