import rsk
import math
import time


def robot_stop(robot):
    robot.control(0., 0., 0.)


while (1):
    with rsk.Client(host='127.0.0.1', key='') as client:
        robot = client.robots['green'][1]
        robot.control(0, 0., 0)
        time.sleep(1)
