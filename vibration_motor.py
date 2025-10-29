def vibration_motor_init(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Vibration Motorz Stufs
def vibration_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def vibration_off(pin):
    GPIO.output(pin, GPIO.LOW)


