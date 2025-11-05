import RPi.GPIO as GPIO

def init(pin, callback_func):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback_func, bouncetime=200)

