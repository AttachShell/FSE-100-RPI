import RPi.GPIO as GPIO
import time

#Ultra Sonic Sensor
SONIC_TRIG = 11
SONIC_ECHO = 12

# Buzzer
BUZZ_PIN = 13

# Vibration Motor
VIBRATION_MOTOR = 16

# Initialization function
def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(SONIC_TRIG, GPIO.OUT)
    GPIO.setup(SONIC_ECHO, GPIO.IN)

    GPIO.setup(BUZZ_PIN, GPIO.OUT)
    GPIO.output(BUZZ_PIN, GPIO.HIGH)

    # Setup for vibration motor
    GPIO.setup(VIBRATION_MOTOR, GPIO.OUT)
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)  # Turn off the vibration motor initially

# Ultrasonic Stufs
def ultrasonic_distance():
    GPIO.output(SONIC_TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(SONIC_TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(SONIC_TRIG, 0)

    while GPIO.input(SONIC_ECHO) == 0:
        pass
    time1 = time.time()
    
    while GPIO.input(SONIC_ECHO) == 1:
        pass
    time2 = time.time()

    duration = time2 - time1
    return (duration * 340 / 2) * 100  # Convert to centimeters

# Buzzer Stufs
def buzzer_on():
    GPIO.output(BUZZ_PIN, GPIO.LOW)  # Turns the buzzer ON

def buzzer_off():
    GPIO.output(BUZZ_PIN, GPIO.HIGH)  # Turns the buzzer OFF

def beep(duration):
    buzzer_on()
    time.sleep(duration)
    buzzer_off()
    time.sleep(duration)

# Vibration Motorz Stufs
def vibration_on():
    GPIO.output(VIBRATION_MOTOR, GPIO.HIGH)

def vibration_off():
    GPIO.output(VIBRATION_MOTOR, GPIO.LOW)

# Runtime Loop
def loop():
    while True:
        ulso_distance = ultrasonic_distance()
        print(ulso_distance, 'cm')  # Print distance measurement

        if ulso_distance < 5:  # If the object is within 5 cm, buzz continuously
            buzzer_on()
            vibration_on()
        elif ulso_distance < 30:  # If within 30 cm, beep with decreasing interval
            beep_interval = (ulso_distance - 5) / 50.0  # Adjust beep interval
            beep(beep_interval)
            vibration_on()
        else:
            buzzer_off()  # Turn off buzzer if object is far
            vibration_off()
        
        time.sleep(0.3)

# Cleanup function
def destroy():
    GPIO.cleanup()  # Reset GPIO settings

# Application Entrypoint
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

