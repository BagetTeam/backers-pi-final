from utils.brick import Motor
from robot_movement.robot_movement import RobotMovement
from color_sensor.color_sensor import ColorSensor
from time import sleep

class LineTracker(RobotMovement):
    def __init__(self, left_motor, right_motor, color_sensor: ColorSensor):
        super().__init__(left_motor, right_motor)
        self.color_sensor = color_sensor
        self.isLeft = False

    def follow_line(self, sensor_reading: int, base_power: int = 30, correction_factor: float = 0.5):
        """
        Adjusts motor speeds based on sensor reading to follow a line.
        
        :param sensor_reading: An integer representing the line sensor's reading.
                               Typically, lower values indicate the line is centered,
                               while higher values indicate deviation.
        :param base_power: The base power level for the motors.
        :param correction_factor: A factor to adjust the speed difference between motors.
        """
        
        # get the color sensor value from the color sensor thread
        # use it to calibrate the middle brightness value.
        # adjust
        # convert color sensor value to a range between -100 to 100
        while True:
            color = self.color_sensor.get_rgb()
            if color[0] < 50 and color[1] < 50 and color[2] < 50: #black
                if self.isLeft:
                    self.adjust_speed(base_power, base_power + 100)
                    self.isLeft = False
                else:
                    self.adjust_speed(base_power + 100, base_power)
                    self.isLeft = True
            sleep(0.01)