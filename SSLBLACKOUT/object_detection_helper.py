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
        """
        Returns the width of the detected object's bounding box.
        If the object is a ball, the width is adjusted to be equal to the maximum of width and height.
        """
        width_w = self.x2 - self.x1
        width_h = self.y2 - self.y1
        if (self.cls == Detected_Object.BALL):
            if (width_w < width_h):
                width_w = width_h
        return width_w
    
    def get_angle_deg(self) -> float:
        """
        Returns the angle of the detected object relative to the center of the image, in degrees.
        """
        object_position = self.get_center()
        image_width = self.get_width()
        fov_degrees = self.CAMERA_FOV
        if(object_position < 0 or object_position >= image_width ):
            raise ValueError("object position is out of bounds of cam resolution.")
        if(fov_degrees > 360 or fov_degrees <= 0):
            raise ValueError("camera FOV is too low or too high.")
        if(image_width <= 0):
            raise ValueError("image_width_is_too_low")
            
        # Calculate the angle of the object relative to the center of the image
        angle_degrees = ((object_position - image_width / 2) /
                        (image_width / 2)) * (fov_degrees / 2)
        return angle_degrees

    def get_height(self) -> int:
        """
        Returns the height of the detected object's bounding box.
        """
        return self.y2 - self.y1

    def get_center(self) -> int:
        """
        Returns the x-coordinate of the center of the detected object's bounding box.
        """
        return self.x1 + (self.get_width()//2)

    def get_estimated_distance(self) -> float:
        """
        Returns the estimated distance to the detected object based on its size and reference distance.
        """
        return (self.ref_size/self.get_width())*self.ref_distance

    def get_info(self):
        """
        Returns a string with information about the detected object.
        """
        return "This object is a " + self.class_name + ".\n" + "It is at a distance of : " + str(self.get_estimated_distance()) + " cm."

    def get_class(self):
        """
        Returns the class name of the detected object.
        """
        return self.class_name
