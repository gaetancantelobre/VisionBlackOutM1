import rsk
import math
import time


def robot_stop(robot):
    robot.control(0., 0., 0.)


with rsk.Client(host='127.0.0.1', key='') as client:
    while(1):
        robot = client.robots['green'][1]
        robot.control(0, -.05, math.radians(20))
