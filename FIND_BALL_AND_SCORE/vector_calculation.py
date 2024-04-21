from math import radians, sin, cos


def get_direction_vector(ball_position, image_width, fov_degrees, distance):
    # Calculate the angle of the ball relative to the center of the image
    angle_degrees = ((ball_position - image_width / 2) /
                     image_width) * fov_degrees
    angle_radians = radians(angle_degrees)

    # Create a direction vector
    direction_vector = [sin(angle_radians),
                        cos(angle_radians), distance]

    return direction_vector


def get_ball_angle(ball_position, image_width, fov_degrees):
    # Calculate the angle of the ball relative to the center of the image
    angle_degrees = ((ball_position - image_width / 2) /
                     (image_width / 2)) * (fov_degrees / 2)
    return angle_degrees
