import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up the GPIO channels - one input and one output
GPIO.setup(12, GPIO.OUT)

# output to pin 12
GPIO.output(12,GPIO.HIGH)
