from gpiozero import MCP3008

class GasSensor:
    def __init__(self, channel):
        self.adc = MCP3008(channel=channel)  # Requires SPI setup

    def get_gas_level(self):
        return self.adc.value  # Value between 0 and 1

# Usage Example
if __name__ == "__main__":
    gas_sensor = GasSensor(channel=1)
    while True:
        print(f"Gas Level: {gas_sensor.get_gas_level():.2f}")
