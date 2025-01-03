from gpiozero import MCP3008

class SoilMoistureSensor:
    def __init__(self, channel):
        self.adc = MCP3008(channel=channel)  # Requires SPI setup

    def get_moisture_level(self):
        return self.adc.value  # Value between 0 (dry) and 1 (wet)

# Usage Example
if __name__ == "__main__":
    soil_sensor = SoilMoistureSensor(channel=0)
    while True:
        print(f"Soil Moisture Level: {soil_sensor.get_moisture_level():.2f}")
