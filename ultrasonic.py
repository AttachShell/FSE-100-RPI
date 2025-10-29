import RPi.GPIO as GPIO
import time

def ultrasonic_init(trig_pin, echo_pin):
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

# Ultrasonic Stufs
def ultrasonic_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, 0)
    time.sleep(0.000002)
    GPIO.output(trig_pin, 1)
    time.sleep(0.00001)
    GPIO.output(trig_pin, 0)

    while GPIO.input(echo_pin) == 0:
        pass
    time1 = time.time()
    
    while GPIO.input(echo_pin) == 1:
        pass
    time2 = time.time()

    duration = time2 - time1
    return (duration * 340 / 2) * 100  # Convert to centimeters


