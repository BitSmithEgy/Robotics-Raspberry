import board
import busio
import adafruit_tcs34725  # Install via pip: pip install adafruit-circuitpython-tcs34725

class ColorSensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)
        self.sensor.integration_time = 100
        self.sensor.gain = 16

    def read_color(self):
        return self.sensor.color

    def read_lux(self):
        return self.sensor.lux

    def read_temperature(self):
        return self.sensor.color_temperature

# Usage Example
if __name__ == "__main__":
    color_sensor = ColorSensor()
    print("Color:", color_sensor.read_color())
    print("Lux:", color_sensor.read_lux())
    print("Temperature (K):", color_sensor.read_temperature())
