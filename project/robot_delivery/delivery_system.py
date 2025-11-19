from time import sleep
from utils.brick import Motor, wait_ready_sensors


class DeliverySystem:
    motor: Motor
    is_active: bool = True
    deg: int = 0
    has_first_been_pushed = False

    def __init__(self, motor: Motor):
        self.motor = motor

    # piston-like delivery system
    def push(self, power: int = 50, duration: float = 0.5):
        angle = 360 if self.has_first_been_pushed else 180

        self.motor.set_position_relative(angle)
        sleep(duration)
