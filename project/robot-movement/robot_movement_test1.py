from time import sleep
from project.utils.brick import (
    Motor,
    reset_brick,
    wait_ready_sensors,
    TouchSensor,
)
import robot_movement

FORWARD_SENSOR = TouchSensor(1)
BACKWARD_SENSOR = TouchSensor(2)
MOTOR1 = Motor("A")
MOTOR2 = Motor("D")

# power const
FWD_POWER = 50
TURNING_POWER = 25

wait_ready_sensors(True)
print("Done waiting")

def main() :
    try:
        # Main loop: runs indefinitely
        while True: 
            while FORWARD_SENSOR.is_pressed():
                robot_movement.move_straight(MOTOR1, MOTOR2, FWD_POWER)
                sleep(0.1)
            while BACKWARD_SENSOR.is_pressed():
                robot_movement.move_straight(MOTOR1,MOTOR2, -FWD_POWER)
                sleep(0.1)
            robot_movement.stop_move(MOTOR1,MOTOR2)
            
    except BaseException:
        pass
    finally:
        print("Done testing")
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    main()


