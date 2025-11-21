from color_sensor.color_sensor import ColorSensor
from utils.brick import (
    EV3GyroSensor,
    Motor,
    TouchSensor,
    EV3ColorSensor,
    reset_brick,
    wait_ready_sensors,
)
from linetracking_system import linetracker, test_linetracker

TOUCH1 = TouchSensor(1)
COLOR = EV3ColorSensor(3)
GYRO = EV3GyroSensor(4)
MOTOR1 = Motor("A")
MOTOR2 = Motor("D")
wait_ready_sensors(True)

GYRO.set_mode("abs")

COLOR_SENSOR = ColorSensor(COLOR)
line_tracker = linetracker.LineTracker(MOTOR1, MOTOR2, COLOR_SENSOR, GYRO)
line_tracker_test = test_linetracker.LineTrackingTest(line_tracker)


def main():
    # movement_test = robot_move_test.MovementTest(TOUCH1, TOUCH2, MOTOR1, MOTOR2)
    try:
        line_tracker_test.test(10, 10)
        # movement_test.corner_turning_test(TURNING_POWER=25)
    except BaseException:
        print("WHYYYYYYYYY hello world")
        pass
    finally:
        print("Done testing")
        COLOR_SENSOR.dispose()
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()


if __name__ == "__main__":
    main()
