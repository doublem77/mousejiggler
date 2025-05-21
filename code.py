import time
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

attesa = 10

while True:
  m.move(x=50, y=50)
  time.sleep(attesa)
  m.move(x=50, y=-50)
  time.sleep(attesa)
  m.move(x=-50, y=-50)
  time.sleep(attesa)
  m.move(x=-50, y=50)
  time.sleep(attesa)