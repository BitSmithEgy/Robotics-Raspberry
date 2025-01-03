from gpiozero import Motor
from time import sleep

class DCMotorController:
    def __init__(self, pin1, pin2, pwm_pin=None):
        """
        Initialize the DC motor controller.
        :param pin1: GPIO pin connected to IN1 on L298N.
        :param pin2: GPIO pin connected to IN2 on L298N.
        :param pwm_pin: GPIO pin connected to ENA on L298N for PWM speed control (optional).
        """
        self.motor = Motor(forward=pin1, backward=pin2, pwm=pwm_pin is not None)
        self.pwm_pin = pwm_pin
        if pwm_pin:
            self.speed = 1  # Default speed (full)
        else:
            self.speed = None  # No PWM control

    def set_speed(self, speed):
        """
        Set motor speed (only if PWM is enabled).
        :param speed: Speed value between 0 (stop) and 1 (full speed).
        """
        if self.pwm_pin is not None:
            self.speed = speed
            self.motor.value = self.speed
        else:
            raise Exception("PWM speed control not enabled for this motor!")

    def forward(self, duration=None):
        """
        Move the motor forward.
        :param duration: Time in seconds to run the motor. If None, runs indefinitely.
        """
        self.motor.forward(self.speed)
        if duration:
            sleep(duration)
            self.stop()

    def backward(self, duration=None):
        """
        Move the motor backward.
        :param duration: Time in seconds to run the motor. If None, runs indefinitely.
        """
        self.motor.backward(self.speed)
        if duration:
            sleep(duration)
            self.stop()

    def stop(self):
        """
        Stop the motor.
        """
        self.motor.stop()

# Example usage
if __name__ == "__main__":
    dc_motor = DCMotorController(pin1=17, pin2=18, pwm_pin=22)
    dc_motor.set_speed(0.8)
    dc_motor.forward(2)
    dc_motor.backward(2)
    dc_motor.stop()
