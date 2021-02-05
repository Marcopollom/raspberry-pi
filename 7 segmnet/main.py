from s_segment import ssegment
import RPi.GPIO as GPIO
import sys
import time


seg = ssegment(37, 35, 33, 31, 40, 38, 36, 3)


if len(sys.argv) < 2:
    while True:
        for i in range(10):
            seg.display(i)
            time.sleep(1)
            seg.reset()
else:
    seg.display(int(sys.argv[1]))



input()
