from time import sleep
from utils.brick import Motor, wait_ready_sensors

class DeliverySystem:
    START_POSITION = 0
    PUSHED_POSITION = 180

    def __init__(self, motor: Motor):
        wait_ready_sensors()
        self.motor = motor
        self.motor.reset_encoder()  # Ensure we start from position 0

    # windmill-like delivery system
    def rotate(self, power: int = 10, duration: float = 1.0):
        self.motor.set_power(power)
        sleep(duration)
        self.motor.set_power(0)

    # piston-like delivery system - pushes 180 degrees out and back
    def push(self, power: int = 50, dps: int = 100):
        self.motor.set_limits(power=power, dps=dps)
        self.motor.set_position(self.PUSHED_POSITION)
        self.motor.wait_is_stopped()  # Wait for motor to reach 180 degrees
        self.motor.set_position(self.START_POSITION)
        self.motor.wait_is_stopped()  # Wait for motor to return to 0 degrees