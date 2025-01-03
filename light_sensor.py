from gpiozero import LightSensor

class LightSensorController:
    def __init__(self, pin):
        self.sensor = LightSensor(pin)

    def get_light_intensity(self):
        return self.sensor.value  # Value between 0 (dark) and 1 (bright)

# Usage Example
if __name__ == "__main__":
    light_sensor = LightSensorController(pin=4)
    while True:
        print(f"Light Intensity: {light_sensor.get_light_intensity():.2f}")
