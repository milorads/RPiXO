import RPi.GPIO as GPIO
import time


pins = {'UL': 25, 'UM': 8, 'UR': 7, 'CL': 17, 'CM': 27, 'CR': 22, 'BL': 10, 'BM': 9, 'BR': 11}


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pinNumber in pins:
    GPIO.setup(pins[pinNumber], GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    UL = GPIO.input(25)
    UM = GPIO.input(8)
    UR = GPIO.input(7)
    CL = GPIO.input(17)
    CM = GPIO.input(27)
    CR = GPIO.input(22)
    BL = GPIO.input(10)
    BM = GPIO.input(9)
    BR = GPIO.input(11)
    if UL == False:
        print('UL Pressed')
        outString = "UL"
        time.sleep(0.2)
        break
    if UM == False:
        print('UM Pressed')
        outString = "UM"
        time.sleep(0.2)
        break
    if UR == False:
        print('UR Pressed')
        outString = "UR"
        time.sleep(0.2)
        break
    if CL == False:
        print('CL Pressed')
        outString = "CL"
        time.sleep(0.2)
        break
    if CM == False:
        print('CM Pressed')
        outString = "CM"
        time.sleep(0.2)
        break
    if CR == False:
        print('CR Pressed')
        outString = "CR"
        time.sleep(0.2)
        break
    if BL == False:
        print('BL Pressed')
        outString = "BL"
        time.sleep(0.2)
        break
    if BM == False:
        print('BM Pressed')
        outString = "BM"
        time.sleep(0.2)
        break
    if BR == False:
        print('BR Pressed')
        outString = "BR"
        time.sleep(0.2)
        break
