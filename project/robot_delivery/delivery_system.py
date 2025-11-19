from time import sleep
from color_sensor.color_sensor import ColorSensor
from utils.brick import Motor, wait_ready_sensors


class DeliverySystem:
    delivery_motor: Motor
    left_motor: Motor
    right_motor: Motor
    sensor: ColorSensor

    is_active: bool = True
    deg: int = 0
    has_first_been_pushed = False

    def __init__(
        self, motor: Motor, left_motor: Motor, right_motor: Motor, sensor: ColorSensor
    ):
        self.delivery_motor = motor
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.sensor = sensor
        self.delivery_motor.reset_encoder()  # Ensure we start from position 0

    def deliver(self):
        color = self.sensor.get_color_detected()

        if color == "GREEN":
            self.move_back()
            self.push()

    def move_back(self, power: int = 50, duration: float = 0):
        self.right_motor.set_position(-100)
        self.right_motor.wait_is_stopped()

    # piston-like delivery system
    def push(self, power: int = 50, duration: float = 0.5):
        angle = 360 if self.has_first_been_pushed else 180
        self.delivery_motor.set_position_relative(angle)
        self.delivery_motor.wait_is_stopped()
