from vector_calculation import get_object_angle


class Detected_Object:
    BALL = 0.0
    ROBOT = 1.0
    GOAL = 2.0
    CAMERA_FOV = 90
    CAMERA_RES = 640

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
        width_w = self.x2 - self.x1
        width_h = self.y2 - self.y1
        if (self.cls == Detected_Object.BALL):
            if (width_w < width_h):
                width_w = width_h
        return width_w

    def get_height(self) -> int:
        return self.y2 - self.y1

    def get_center(self) -> int:
        return self.x1 + (self.get_width()//2)

    def get_estimated_distance(self) -> float:
        return (self.ref_size/self.get_width())*self.ref_distance

    def get_angle_deg(self) -> float:
        return get_object_angle(self.get_center(), self.CAMERA_RES, self.CAMERA_FOV)

    def get_info(self):
        return "This object is a " + self.class_name + ".\n" + "It is at a distance of : " + str(self.get_estimated_distance()) + " cm."

    def get_class(self):
        return self.class_name
