from time import sleep
import delivery_system as deliv_sys
from utils.brick import TouchSensor, Motor

ROTATE_BUTTON = TouchSensor(1);
MOTOR = Motor("A")

class DeliveryTest:
    def __init__(self, motor: Motor):
        self.delivery_system = deliv_sys.DeliverySystem(motor)

    def rotate_test(self, ROTATE_POWER: int = 10, ROTATE_TIME: float = 1.0):
        # Main loop: runs indefinitely
        while True: 
            while ROTATE_BUTTON.is_pressed():
                sleep(0.1)
            self.delivery_system.rotate(ROTATE_POWER, ROTATE_TIME)
            while not ROTATE_BUTTON.is_pressed():
                sleep(0.1)

    def push_test(self, PUSH_POWER: int = 50, PUSH_TIME: float = 0.5):
        # Main loop: runs indefinitely
        while True: 
            while ROTATE_BUTTON.is_pressed():
                sleep(0.1)
            self.delivery_system.push(PUSH_POWER, PUSH_TIME)
            while not ROTATE_BUTTON.is_pressed():
                sleep(0.1)