from time import sleep
from color_sensor.color_sensor import ColorSensor
from utils.brick import Motor, wait_ready_sensors
from robot_movement.robot_movement import RobotMovement
from robot_delivery.delivery_system import DeliverySystem

MOTOR_POWER = 30

class ZoneDetection:
    color_sensor: ColorSensor
    delivery_motor: Motor
    left_motor: Motor
    right_motor: Motor

    def __init__(self, color_sensor, deliv_motor, left_motor, right_motor):
        self.color_sensor = color_sensor
        self.delivery_motor = deliv_motor
        self.left_motor = left_motor
        self.right_motor = right_motor
        
    def detect_zones(self) :
        movement = RobotMovement(self.left_motor, self.right_motor)
        delivery = DeliverySystem(self.delivery_motor, self.left_motor, self.right_motor,)
        while True:
            color = self.color_sensor.current_color
            if color == "ORANGE":
                movement.move_straight(-MOTOR_POWER)
                sleep(0.5)
                movement.corner_turn_left(MOTOR_POWER)
                sleep(0.5)
                # movement.move_straight(MOTOR_POWER)
                # sleep(x)
                movement.corner_turn_right(MOTOR_POWER)
                sleep(0.5)
                movement.move_straight(MOTOR_POWER)
            elif color == "GREEN":
                movement.stop_move()
                sleep(0.3)
                delivery.deliver()
                sleep(0.3)
                movement.change_relative_angle(-360, 360)
                sleep(0.3)
                movement.move_straight(MOTOR_POWER)

            elif color == "RED":
                movement.stop_move()
                sleep(0.3)
                movement.change_relative_angle(-360,360)
                sleep(0.3)
                movement.move_straight(MOTOR_POWER)
