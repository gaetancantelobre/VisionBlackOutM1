

class Detected_Object:
    BALL = 0.0
    ROBOT = 1.0
    GOAL = 2.0

    def __init__(self, cls, bounding_box) -> None:
        self.x1, self.y1, self.x2, self.y2 = bounding_box
        self.cls = cls
        if (cls == self.BALL):
            self.class_name = "Ball"
            self.ref_size = 65
            self.ref_distance = 30
        elif (cls == 1.0):
            self.class_name = "Robot"
            self.ref_size = 70
            self.ref_distance = 171
        elif (cls == 2.0):
            self.class_name = "Goal"
            self.ref_size = 280
            self.ref_distance = 171

    def get_width(self) -> int:
        return self.x2 - self.x1

    def get_center(self) -> int:
        return self.x1 + (self.get_center()//2)

    def get_estimated_distance(self) -> float:
        return self.ref_size/(self.get_width()*self.ref_distance)
