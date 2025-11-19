from color_sensor.color_sensor import ColorSensor
from linetracking_system.linetracker import LineTracker
from robot_movement.robot_movement import RobotMovement

class LineTrackingTest:
    def __init__(self, robot_movement: RobotMovement, color_sensor: ColorSensor):
        self.linetracking = LineTracker(robot_movement, color_sensor)
    
    def test(self, base_power, correction_factor):
        self.linetracking.follow_line3(base_power=base_power, correction_factor=correction_factor)