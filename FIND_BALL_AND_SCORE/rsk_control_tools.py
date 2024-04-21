from rsk import control
from time import sleep


def robot_stop(robot):
    # sets the all velocities of a robot to 0 making it stop completely
    robot.control(0., 0., 0.)


def shoot(robot):
    # makes the robot speed forward to push the ball
    # then use the kicker to push it further
    robot.control(10, 0, 0)
    sleep(1)
    robot_stop(robot)
    robot.kick()
