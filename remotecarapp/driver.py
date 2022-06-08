# Pin Layout
# USB & Ether downside
#
#                   1     2  <---> 5V
#                   3     4  <---> 5V
#                   5     6  <---> Ground
#                   7     8  
#                   9     10 
#     GPIO 17 <---> 11    12
#     GPIO 27 <---> 13    14
#     GPIO 22 <---> 15    16 <---> GPIO 23
#                   17    18 <---> GPIO 24
#                   19    20
#                   21    22
#                   23    24
#                   25    26
#                   27    28
#                   29    30
#                   31    32
#                   33    34
#                   35    36
#                   37    38
#                   39    40
#
#
#   GPIO 17     left  forward
#   GPIO 27     left  backward
#   GPIO 23     right forward
#   GPIO 24     right backward
#   GPIO 22     LED



# Imports
#import RPi.GPIO as GPIO
import time


# Fictional Django Input
driver_IN = ""

# Pins
leftFWD = 17    # pin for left forward drive
leftBWD = 27    # pin for left backward drive
rightFWD = 23   # pin for right forward drive
rightBWD = 24   # pin for right backward drive
pinList = [leftFWD, leftBWD, rightFWD, rightBWD]

for pin in pinList:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)
    pass

# Pin-Input Dict
pinin_dict = {
    "leftFWD"  : leftFWD,
    "leftBWD"  : leftFWD,
    "rightFWD" : rightFWD,
    "rightFWD" : rightBWD
}

# Clean dir Dict
clearDirDict = {
    "leftFWD"  : "Left Forward",
    "leftBWD"  : "Left Backward",
    "rightFWD" : "Right Forward",
    "rightBWD" : "Right Backward"
}


# Blinker
def blink(pin):
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)


# Drive function
def drive(direct, durr = 1):
        print(f"Turned {durr} seconds in {clearDirDict[direct]}")
       
        if direct == "fwd":
            GPIO.output(leftFWD, GPIO.HIGH)
            GPIO.output(rightFWD, GPIO.HIGH)
            time.sleep(durr)
            GPIO.output(leftFWD, GPIO.LOW)
            GPIO.output(rightFWD, GPIO.LOW)
        
        elif direct == "bwd":
            GPIO.output(leftBWD, GPIO.HIGH)
            GPIO.output(rightBWD, GPIO.HIGH)
            time.sleep(durr)
            GPIO.output(leftBWD, GPIO.LOW)
            GPIO.output(rightBWD, GPIO.LOW)


# Turn function
def turn(direct, durr = 1):
    if direct == "l":
        GPIO.output(leftFWD, GPIO.HIGH)
        GPIO.output(rightBWD, GPIO.HIGH)
        time.sleep(durr)
        GPIO.output(leftFWD, GPIO.LOW)
        GPIO.output(rightBWD, GPIO.LOW)

    if direct == "r":
        GPIO.output(rightFWD, GPIO.HIGH)
        GPIO.output(leftBWD, GPIO.HIGH)
        time.sleep(durr)
        GPIO.output(rightFWD, GPIO.LOW)
        GPIO.output(leftBWD, GPIO.LOW)

turn("rightFWD")


def test():
    print("Test complete")
    

GPIO.setmode(GPIO.BCM)      #Call pins by number



