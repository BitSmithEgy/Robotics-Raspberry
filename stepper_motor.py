import RPi.GPIO as GPIO
from time import sleep

class StepperMotorController:
    def __init__(self, step_pin, dir_pin, enable_pin=None):
        """
        Initialize the stepper motor controller.
        :param step_pin: GPIO pin connected to the STEP pin.
        :param dir_pin: GPIO pin connected to the DIR pin.
        :param enable_pin: GPIO pin connected to the ENABLE pin (optional).
        """
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.enable_pin = enable_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

        if self.enable_pin:
            GPIO.setup(self.enable_pin, GPIO.OUT)
            self.disable()

    def enable(self):
        """Enable the stepper motor (if enable pin is used)."""
        if self.enable_pin:
            GPIO.output(self.enable_pin, GPIO.LOW)

    def disable(self):
        """Disable the stepper motor (if enable pin is used)."""
        if self.enable_pin:
            GPIO.output(self.enable_pin, GPIO.HIGH)

    def rotate(self, steps, direction=True, delay=0.001):
        """
        Rotate the stepper motor.
        :param steps: Number of steps to rotate.
        :param direction: Direction of rotation (True for clockwise, False for counterclockwise).
        :param delay: Delay between steps (affects speed).
        """
        GPIO.output(self.dir_pin, GPIO.HIGH if direction else GPIO.LOW)
        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(delay)

    def cleanup(self):
        """Clean up GPIO resources."""
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    stepper = StepperMotorController(step_pin=20, dir_pin=21, enable_pin=16)
    stepper.enable()
    stepper.rotate(steps=200, direction=True, delay=0.002)  # 200 steps clockwise
    sleep(1)
    stepper.rotate(steps=200, direction=False, delay=0.002)  # 200 steps counterclockwise
    stepper.disable()
    stepper.cleanup()
