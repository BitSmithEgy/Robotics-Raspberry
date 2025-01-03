from gpiozero import MotionSensor

class PIRMotionSensor:
    def __init__(self, pin):
        self.sensor = MotionSensor(pin)

    def is_motion_detected(self):
        return self.sensor.motion_detected

# Usage Example
if __name__ == "__main__":
    pir_sensor = PIRMotionSensor(pin=17)
    while True:
        if pir_sensor.is_motion_detected():
            print("Motion detected!")
        else:
            print("No motion.")
