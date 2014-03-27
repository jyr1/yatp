import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up the GPIO channels - one input and one output
GPIO.setup(15, GPIO.OUT)

# output to pin 15
x=0
while x < 50 :
	x=x+1
	print "on"
	GPIO.output(15, GPIO.HIGH)
	time.sleep(3)
	print "off"
	GPIO.output(15, GPIO.LOW)
	time.sleep(3)
