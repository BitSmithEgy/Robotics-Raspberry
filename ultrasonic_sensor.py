from gpiozero import DistanceSensor

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

    def get_distance(self):
        return self.sensor.distance * 100  # Convert to centimeters

# Usage Example
if __name__ == "__main__":
    ultrasonic = UltrasonicSensor(trigger_pin=18, echo_pin=24)
    while True:
        print(f"Distance: {ultrasonic.get_distance():.2f} cm")
