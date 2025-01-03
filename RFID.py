import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522  # Install via pip: pip install mfrc522

class RFIDReader:
    def __init__(self):
        self.reader = SimpleMFRC522()

    def read_card(self):
        try:
            id, text = self.reader.read()
            return {"id": id, "text": text}
        except Exception as e:
            print(f"Error reading card: {e}")
            return None

# Usage Example
if __name__ == "__main__":
    rfid = RFIDReader()
    print("Hold a card near the reader...")
    data = rfid.read_card()
    if data:
        print(f"ID: {data['id']}, Text: {data['text']}")
