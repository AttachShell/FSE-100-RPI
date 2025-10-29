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

    ultrasonic_init(SONIC_TRIG, SONIC_ECHO) 
    buzzer_init(BUZZ_PIN)
    vibration_motor_init(VIBRATION_MOTOR)

# Runtime Loop
def loop():
    while True:
        ulso_distance = ultrasonic_distance(SONIC_TRIG, SONIC_ECHO)
        print(ulso_distance, 'cm')  # Print distance measurement

        if ulso_distance < 10:  # If the object is within 5 cm, buzz continuously
            # buzzer_on()
            buzzer_on(BUZZ_PIN)
        elif ulso_distance < 30:  # If within 30 cm, beep with decreasing interval
           # beep_interval = (ulso_distance - 5) / 50.0  # Adjust beep interval
           # beep(beep_interval)
            vibration_on(VIBRATION_MOTOR)
        else:
           # buzzer_off()  # Turn off buzzer if object is far
            vibration_off(VIBRATION_MOTOR)
        
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

