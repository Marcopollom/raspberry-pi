from s_segment import ssegment
import RPi.GPIO as GPIO
import sys
import time


seg = ssegment(37, 35, 33, 31, 40, 38, 36, 3)

bitmap = {
    0: 0b00111111,
    1: 0b00000110,
    2: 0b01011011,
    3: 0b01001111,
    4: 0b01100110,
    5: 0b01101101, 
    6: 0b01111101,
    7: 0b00000111,
    8: 0b01111111,
    9: 0b01100111 
}

charMap = {
    'a': 0b00000001,
    'b': 0b00000010,
    'c': 0b00000100,
    'd': 0b00001000,
    'e': 0b00010000,
    'f': 0b00100000,
    'g': 0b01000000
}


pinMap ={
    'a': seg.a,
    'b': seg.b,
    'c': seg.c,
    'd': seg.d,
    'e': seg.e,
    'f': seg.f,
    'g': seg.g
}


def display(n):
    value = bitmap[n]

    GPIO.output(list(pinMap.values()), GPIO.HIGH)

    for i, e in charMap.items():
        if value & e == e:
            GPIO.output(pinMap[i], GPIO.LOW)



if len(sys.argv) < 2:
    while True:
        for i in range(10):
            display(i)
            time.sleep(1)
            GPIO.output(list(pinMap.values()), GPIO.HIGH)
            
else:
    display(int(sys.argv[1]))



input()
