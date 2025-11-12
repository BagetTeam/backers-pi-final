from time import sleep
from project.utils.brick import (
    Motor,
    reset_brick,
    wait_ready_sensors,
    TouchSensor,
)
import robot_movement as rbt_mvt

RIGHT_SENSOR = TouchSensor(1)
LEFT_SENSOR = TouchSensor(2)
MOTOR1 = Motor("A")
MOTOR2 = Motor("D")

robot_movement = rbt_mvt.RobotMovement(MOTOR1, MOTOR2)


# power const
FWD_POWER = 50
TURNING_POWER = 25

wait_ready_sensors(True)
print("Done waiting")

def main() :
    try:
        # Main loop: runs indefinitely
        while True: 
            while RIGHT_SENSOR.is_pressed():
                robot_movement.turn_right(TURNING_POWER)
                sleep(0.1)
            while LEFT_SENSOR.is_pressed():
                robot_movement.turn_left(TURNING_POWER)
                sleep(0.1)
            robot_movement.stop_move()
    except BaseException:
        pass
    finally:
        print("Done testing")
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    main()