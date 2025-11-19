from utils.brick import (
    Motor,
    TouchSensor,
    reset_brick,
    wait_ready_sensors,
)


def main():
    motor = Motor("D")
    touch = TouchSensor(1)
    wait_ready_sensors(True)

    deg = 0
    motor.set_position_relative(180)

    while True:
        deg = motor.get_position()
        pass


if __name__ == "__main__":
    try:
        main()

    except BaseException:
        pass
    finally:
        print("Done testing")
        reset_brick()  # Turn off everything on the brick's hardware, and reset it
        exit()
