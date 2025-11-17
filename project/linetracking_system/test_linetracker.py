from linetracker import LineTracker

class LineTrackingTest:
    def __init__(self, linetracking: LineTracker):
        self.linetracking = linetracking
    
    def test(self):
        self.linetracking.follow_line()