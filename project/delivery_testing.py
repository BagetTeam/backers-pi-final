from robot_delivery.delivery_system import DeliverySystem
from utils.brick import Motor, wait_ready_sensors

motor = Motor("C")
wait_ready_sensors(True)

delivery_system = DeliverySystem(motor)


def main():
    pass


if __name__ == "__main__":
    main()
