from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor

class ColorSensor:
    def __init__(self, sensor: EV3ColorSensor):
        wait_ready_sensors()
        self.sensor = sensor

    def get_rgb(self) -> list[float]:
        return self.sensor.get_rgb()
    
    def classify_color(self) -> str:
        rgb = self.get_rgb()
        red, green, blue = rgb

        if red > green and red > blue:
            return "red"
        elif green > red and green > blue:
            return "green"
        elif blue > red and blue > green:
            return "blue"
        else:
            return "unknown"
    
    def __normalize_rgb(self, rgb: list[float]) -> list[float]:
        total = sum(rgb)
        if total == 0:
            return [0.0, 0.0, 0.0]
        return [value / total for value in rgb]
    
    def is_color_detected(self, target_color: str, threshold: float = 0.1) -> bool:
        rgb = self.get_rgb()
        normalized_rgb = self.__normalize_rgb(rgb)
        red, green, blue = normalized_rgb

        if target_color == "red":
            return red > green + threshold and red > blue + threshold
        elif target_color == "green":
            return green > red + threshold and green > blue + threshold
        elif target_color == "blue":
            return blue > red + threshold and blue > green + threshold
        else:
            return False
    

    