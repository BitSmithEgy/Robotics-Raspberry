import Adafruit_DHT  # Install via pip: pip install Adafruit_DHT

class TemperatureHumiditySensor:
    def __init__(self, sensor_type, pin):
        self.sensor_type = sensor_type  # Adafruit_DHT.DHT11 or Adafruit_DHT.DHT22
        self.pin = pin

    def read_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
        if humidity is not None and temperature is not None:
            return {"temperature": temperature, "humidity": humidity}
        else:
            return None

# Usage Example
if __name__ == "__main__":
    dht_sensor = TemperatureHumiditySensor(Adafruit_DHT.DHT22, pin=4)
    data = dht_sensor.read_data()
    if data:
        print(f"Temperature: {data['temperature']:.2f}°C, Humidity: {data['humidity']:.2f}%")
    else:
        print("Failed to read from DHT sensor.")
