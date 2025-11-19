from  time import sleep
from zone_detection.zone_detection import ZoneDetection
from robot_movement.robot_movement import RobotMovement
from utils.brick import TouchSensor, Motor
from threading import Thread

class ZoneTest:
    def __init__(self, zonedetect: ZoneDetection, touchsensor: TouchSensor, left_motor: Motor, right_motor: Motor):
        self.zone_detection = zonedetect
        self.touch_sensor = touchsensor
        self.left_motor = left_motor
        self.right_motor = right_motor

    def test(self):
        thread = Thread(target=self.zone_detection.detect_zones)
        thread.start()
        
        movement = RobotMovement(self.left_motor, self.right_motor)
        while True:
            while self.touch_sensor.is_pressed():
                movement.move_straight(30)
                sleep(0.1)
            movement.stop_move()