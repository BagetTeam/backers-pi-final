from utils.brick import (
    Motor,
    TouchSensor,
    EV3ColorSensor,
    reset_brick,
    configure_ports,
)
from robot_movement import robot_movement_test as robot_move_test
from linetracking_system import linetracker, test_linetracker

TOUCH1, COLOR, MOTOR1, MOTOR2 = configure_ports(
    PORT_1=TouchSensor,
    PORT_2=EV3ColorSensor,
    PORT_A=Motor,
    PORT_D=Motor,
    wait=True,
    print_status=True,
)

def main():
    # movement_test = robot_move_test.MovementTest(TOUCH1, TOUCH2, MOTOR1, MOTOR2)
    line_tracker = linetracker.LineTracker(MOTOR1, MOTOR2, COLOR)
    line_tracker_test = test_linetracker.LineTrackingTest(line_tracker)
    try:
        line_tracker_test.test(10, 10)
        # movement_test.corner_turning_test(TURNING_POWER=25)
    except BaseException:
        pass
    finally:
        print("Done testing")
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    main()