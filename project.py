import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
from datetime import datetime


def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)  # Actived LCD using CS
    time.sleep(0.000005)


def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)  # Deactived LCD using CS
    time.sleep(0.000005)


# setup lcd
PIN_OUT = {
    "SCLK": 14,
    "DIN": 11,
    "DC": 9,
    "CS": 15,  # We will not connect this pin! --> we use w13
    "RST": 10,
    "LED": 6,  # backlight
}

counter = 1
buttonState = 0
lastButtonState = 0
buttonPin = 1
ledpin = 15
pin_CS_lcd = 13
wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  # (channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd, 1)  # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(buttonPin, 0)
wiringpi.pinMode(ledpin, 1)
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

i = 90
try:
    lcd_1.clear()
    while True:
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(datetime.now().strftime("%m/%d/%Y"))
        lcd_1.go_to_xy(0, 10)
        lcd_1.put_string(datetime.now().strftime("%H:%M:%S"))
        lcd_1.refresh()
        DeactivateLCD()
        buttonState = wiringpi.digitalRead(buttonPin)
        if buttonState != lastButtonState:
            if buttonState == True:
                counter += 1
        else:
            time.sleep(0.05)
        lastButtonState = buttonState

        if counter % 2 == 0:
            wiringpi.digitalWrite(ledpin, 1)
        else:
            wiringpi.digitalWrite(ledpin, 0)
except KeyboardInterrupt:
    wiringpi.digitalWrite(ledpin, 0)
    lcd_1.clear()
    lcd_1.refresh()
    DeactivateLCD()
    print("\nProgram terminated")
