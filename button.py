import RPi.GPIO as GPIO

def init(pin):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=detect, bouncetime=200)

def detect(change):
    print("button: " + change + ", " + GPIO.input(15))

