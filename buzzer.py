import RPi.GPIO as GPIO
import time

def buzzer_init(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Buzzer Stufs
def buzzer_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turns the buzzer ON

def buzzer_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turns the buzzer OFF

def beep(duration, pin):
    buzzer_on(pin)
    time.sleep(duration)
    buzzer_off(pin)
    time.sleep(duration)
