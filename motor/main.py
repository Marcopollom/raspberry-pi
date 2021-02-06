from motor import motor
import time
import sys

def main():

    motor1 = motor(7, 11, 15)

    if len(sys.argv) > 2 and sys.argv[1] == 's':
        motor1.stop()
        print("Motor Stopped")
	
	return 0
    


    motor1.backward()

    time.sleep(2.5)

    motor1.speed(50)
    motor1.forward()
    
    time.sleep(2.5)

    motor1.stop()

if __name__ == '__main__':
    main()

