from rsk import control
from time import sleep
from object_detection_helper import Detected_Object
from math import radians

from vector_calculation import *


class Robot_controller:
    
    # STATUS
    # 0 waiting
    # 1 working
    # 2 task completed
    STATUS = 0
    
    MAX_SPEED = 3
    MIN_SPEED = 0.05
    control_vector = (0.0,0.0,0.0)
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
    
    
    def reset_objects(self):
        self.BALL = None
        self.GOAL = None
        self.ROBOTS = []
        return
    
    
    def get_status(self):
        return self.STATUS
  
    def __init__(self, robot,min_visibility_distance) -> None:
        self.robot = robot
        self.NO_VISIBLITY_LIMIT_DISTANCE = min_visibility_distance
        
    
    def set_control_vector(self, vector3):
        for i in range(2):
            vector3[i] = self.MAX_SPEED if vector3[i] > self.MAX_SPEED else vector3[i]
            vector3[i] = self.MIN_SPEED if vector3[i] < self.MIN_SPEED else vector3[i]
        self.control_vector = vector3
        return
        
    def shoot(self):
        self.set_control_vector_deg((self.MAX_SPEED,0,0))
        self.move
        sleep(1)
        self.stop()
        self.robot.kick()
        return
        
    def stop(self):
        # sets the all velocities of a robot to 0 making it stop completely
        self.set_control_vector_deg((0,0,0))
        self.move()
        return
        
    def get_control_vector(self):
        return self.control_vector
    
    def move(self):
        self.robot.control(self.control_vector[0],self.control_vector[1],self.control_vector[2])
        return
    
    def rotate_on_self(self):
        self.set_control_vector_deg((0., 0, math.radians(30)*-1))
        self.move()
        
    def oribit_around_ball(self):
        self.set_control_vector((0, self.MIN_SPEED, radians(20)))
    
    def is_object_detected(self):
        for obj in self.OBJECT_LIST:
            if obj.get_class() == "Ball":
                self.BALL == obj
            elif(obj.get_class() == "Goal"):
                self.GOAL = obj
            elif(obj.get_class() == "Robot"):
                self.ROBOT.append(obj)
        return
    
    def is_goal_centered(self):
        goal_is_centered = (self.GOAL.get_center() >= 150 and self.GOAL.get_center() <= 450 and self.GOAL.get_width() > 200)

    
    def find_ball(self):
        self.reset_objects()
        self.is_object_detected()
        
        if(self.get_status() == 2): # if operation is finished we wait for the next command
            self.stop()
            return 
        self.STATUS = 1
        
        if(self.BALL == None):
            self.rotate_on_self()
        elif self.BALL != None:
            if(self.BALL.get_estimated_distance() > self.NO_VISIBLITY_LIMIT_DISTANCE):
                dist = self.BALL.get_estimated_distance()
                speed = get_speed_from_distance(dist)
                angle_deg = self.BALL.get_angle_deg()
                self.set_control_vector((speed,0,round(radians(angle_deg))*-1)) # we round the float value and make it negative to turn in the right direction
                self.move()
            elif(self.BALL.get_estimated_distance() < self.NO_VISIBLITY_LIMIT_DISTANCE):
                self.BALL_APPROACHED = 1
                self.stop()
                self.STATUS = 2
                return
        self.STATUS = 1
    
    def find_goal_and_score(self):
        self.reset_objects()
        self.is_object_detected()
        if(self.get_status() == 2): # if operation is finished we wait for the next command
            self.stop()
            return
        if(self.BALL_APPROACHED != 1):
            self.find_ball(self)   
        else:
            if(self.GOAL != None):
                self.is_goal_centered()
                if(self.GOAL_CENTERED):
                    self.shoot()                
                    self.STATUS = 2
            self.oribit_around_ball()
            self.STATUS = 1
            
     
    def find_ball_and_score(self):
        if(self.get_status ==2 and cpt == 1):
            self.reset_all()
            return 1
        
        if(self.get_status() == 0):
            self.STATUS = 1
        
        if(self.get_status() == 2):
            cpt = cpt + 1
            
        if(self.get_status() == 1):
            if(cpt == 0):
                self.find_ball()
            elif(cpt == 1):
                self.find_goal_and_score()
            
            
    
