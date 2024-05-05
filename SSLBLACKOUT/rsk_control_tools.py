from rsk import control
from time import sleep
from math import radians

from .vector_calculation import *


class Robot_controller:

    # STATUS
    # 0 waiting
    # 1 working
    # 2 task completed
    STATUS = 0

    # MODIFY BASE VALUES TO ADJUST ON THE FLY
    MAX_SPEED = 3
    MIN_SPEED = 0.05
    control_vector = (0.0, 0.0, 0.0)
    NO_VISIBLITY_LIMIT_DISTANCE = 0

    OBJECT_LIST = []  # list of detected objects
    BALL = None
    GOAL = None
    ROBOT = []

    OPERATION_STEP = 0

    BALL_APPROACHED = 0
    GOAL_CENTERED = 0

    def reset_status(self):
        self.STATUS = 0
        return

    # resets object references

    def reset_objects(self):
        self.BALL = None
        self.GOAL = None
        self.ROBOTS = []
        return

    def reset_all(self):
        """
        Resets the status and objects of the robot controller.
        """
        self.reset_status()
        self.reset_objects()
        return

    def set_control_vector_deg(self, vector3):
        """
        Sets the control vector of the robot controller using degrees.
        """
        vector3_rad = [radians(angle) for angle in vector3]
        self.set_control_vector(vector3_rad)
        return

    def get_status(self):
        """
        Returns the current status of the robot controller.
        """
        return self.STATUS

    def move_to_goal(self):
        """
        Moves the robot towards the goal.
        """
        if self.GOAL is not None:
            dist = self.GOAL.get_estimated_distance()
            speed = get_speed_from_distance(dist)
            angle_deg = self.GOAL.get_angle_deg()
            self.set_control_vector((speed, 0, round(radians(angle_deg)) * -1))
            self.move()
        return

    def find_ball(self):
        """
        Finds the ball and adjusts the robot's movement accordingly.
        """
        self.reset_objects()
        self.is_object_detected()

        if self.get_status() == 2:  # if operation is finished we wait for the next command
            self.stop()
            return
        self.STATUS = 1

        if self.BALL is None:
            self.rotate_on_self()
        elif self.BALL is not None:
            if self.BALL.get_estimated_distance() > self.NO_VISIBLITY_LIMIT_DISTANCE:
                dist = self.BALL.get_estimated_distance()
                speed = get_speed_from_distance(dist)
                angle_deg = self.BALL.get_angle_deg()
                # we round the float value and make it negative to turn in the right direction
                self.set_control_vector(
                    (speed, 0, round(radians(angle_deg)) * -1))
                self.move()
            elif self.BALL.get_estimated_distance() < self.NO_VISIBLITY_LIMIT_DISTANCE:
                self.BALL_APPROACHED = 1
                self.stop()
                self.STATUS = 2
                return
        self.STATUS = 1

    def find_goal_and_score(self):
        """
        Finds the goal and scores if it is centered.
        """
        self.reset_objects()
        self.is_object_detected()
        if self.get_status() == 2:  # if operation is finished we wait for the next command
            self.stop()
            return
        if self.BALL_APPROACHED != 1:
            self.find_ball()
        else:
            if self.GOAL is not None:
                self.is_goal_centered()
                if self.GOAL_CENTERED:
                    self.shoot()
                    self.STATUS = 2
            self.oribit_around_ball()
            self.STATUS = 1

    def find_ball_and_score(self, obj_list):
        """
        Finds the ball and scores if the goal is centered.
        """
        self.OBJECT_LIST = obj_list
        if self.get_status() == 2 and cpt == 1:
            self.reset_all()
            return 1

        if self.get_status() == 0:
            self.STATUS = 1

        if self.get_status() == 2:
            cpt = cpt + 1

        if self.get_status() == 1:
            if cpt == 0:
                self.find_ball()
            elif cpt == 1:
                self.find_goal_and_score()
