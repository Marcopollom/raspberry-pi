from datetime import datetime
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

def clock(seg):
    it = 0.5
    
    while True:
        now = datetime.now()
        seg.text = now.strftime("%H-%M-%S")
        time.sleep(it)


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)

clock(seg)



