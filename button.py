import RPi.GPIO as GPIO

local_callback_func=print("Button Callback Not Assigned!")

def init(pin, callback_func):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback, bouncetime=200)
    local_callback_func = callback_func

def callback(chn):
    local_callback_func();
