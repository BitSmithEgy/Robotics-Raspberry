from gpiozero import DigitalInputDevice

class IRSensor:
    def __init__(self, pin):
        self.sensor = DigitalInputDevice(pin)

    def is_object_detected(self):
        return not self.sensor.value  # Assuming active-low signal

# Usage Example
if __name__ == "__main__":
    ir_sensor = IRSensor(pin=17)
    while True:
        if ir_sensor.is_object_detected():
            print("Object detected!")
        else:
            print("No object detected.")
