import RPi.GPIO as GPIO
import time

import ultrasonic
import vibration_motor as vibration
import buzzer
import button

# These pin numbers are based on the physical locals on the board

#Ultra Sonic Sensor
SONIC_TRIG = 11
SONIC_ECHO = 12

# Buzzer
BUZZ_PIN = 13

# Vibration Motor
VIBRATION_MOTOR = 16

# Button
BUTTON_PIN = 12

# Initialization function
def setup():
    GPIO.setmode(GPIO.BOARD)

    ultrasonic.ultrasonic_init(SONIC_TRIG, SONIC_ECHO) 
    buzzer.buzzer_init(BUZZ_PIN)
    vibration.vibration_motor_init(VIBRATION_MOTOR)
    button.init(BUTTON_PIN)

# Runtime Loop
def loop():
    while True:
        ulso_distance = ultrasonic.ultrasonic_distance(SONIC_TRIG, SONIC_ECHO)
        print(ulso_distance, 'cm')  # Print distance measurement

        if ulso_distance < 10:  # If the object is within 5 cm, buzz continuously
            # buzzer_on()
            buzzer.buzzer_on(BUZZ_PIN)
        elif ulso_distance < 30:  # If within 30 cm, beep with decreasing interval
           # beep_interval = (ulso_distance - 5) / 50.0  # Adjust beep interval
           # beep(beep_interval)
            vibration.vibration_on(VIBRATION_MOTOR)
            buzzer.buzzer_off(BUZZ_PIN)
        else:
           # buzzer_off()  # Turn off buzzer if object is far
            vibration.vibration_off(VIBRATION_MOTOR)
            buzzer.buzzer_off(BUZZ_PIN)
        
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

