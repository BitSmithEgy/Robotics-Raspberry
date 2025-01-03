from gpiozero import Servo
from time import sleep

class ServoMotor:
    def __init__(self, pin):
        self.servo = Servo(pin)

    def set_angle(self, angle):
        # Map angle (0 to 180) to -1 (min) to 1 (max)
        self.servo.value = (angle / 180) * 2 - 1

# Usage Example
if __name__ == "__main__":
    servo = ServoMotor(pin=17)
    for angle in range(0, 181, 10):
        servo.set_angle(angle)
        print(f"Servo Angle: {angle}")
        sleep(0.5)
