from gpiozero import Buzzer
from time import sleep

class BuzzerController:
    def __init__(self, pin):
        self.buzzer = Buzzer(pin)

    def beep(self, duration=1):
        self.buzzer.on()
        sleep(duration)
        self.buzzer.off()

# Usage Example
if __name__ == "__main__":
    buzzer = BuzzerController(pin=18)
    buzzer.beep(0.5)
