from time import sleep
from color_sensor.color_sensor import ColorSensor
from robot_movement.robot_movement import RobotMovement
from robot_delivery.delivery_system import DeliverySystem
from utils.brick import EV3ColorSensor, Motor, reset_brick, wait_ready_sensors

motor = Motor("C")
left_motor = Motor("A")
right_motor = Motor("D")
sensor = EV3ColorSensor(3)
wait_ready_sensors(True)

color_sensor = ColorSensor(sensor)
delivery_system = DeliverySystem(motor, color_sensor, right_motor)


def main():
    try:
        delivery_system.deliver()
    finally:
        color_sensor.dispose()
        reset_brick()
        exit()


if __name__ == "__main__":
    main()
