from math import radians, sin, cos


def get_direction_vector(ball_position, image_width, fov_degrees, distance):
    """
    Calculates the direction vector based on the ball position, image width, field of view (FOV) in degrees, and distance.

    Args:
        ball_position (float): The position of the ball.
        image_width (int): The width of the image.
        fov_degrees (float): The field of view (FOV) in degrees.
        distance (float): The distance.

    Returns:
        list: The direction vector [x, y, z].
    """
    # Calculate the angle in degrees based on the ball position and image width
    angle_degrees = ((ball_position - image_width / 2) /
                     image_width) * fov_degrees

    # Convert the angle to radians
    angle_radians = radians(angle_degrees)

    # Create a direction vector using sin and cos of the angle, and the distance
    direction_vector = [sin(angle_radians),
                        cos(angle_radians), distance]

    return direction_vector


def get_object_angle(object_position, image_width, fov_degrees):
    """
    Calculates the angle of the object relative to the center of the image.

    Args:
        object_position (float): The position of the object.
        image_width (int): The width of the image.
        fov_degrees (float): The field of view (FOV) in degrees.

    Returns:
        float: The angle of the object in degrees.
    """
    # Check if the object position is within the image bounds
    if object_position < 0 or object_position >= image_width:
        raise ValueError(
            "Object position is out of bounds of the camera resolution.")

    # Check if the FOV is within a valid range
    if fov_degrees > 360 or fov_degrees <= 0:
        raise ValueError("Camera FOV is too low or too high.")

    # Check if the image width is valid
    if image_width <= 0:
        raise ValueError("Image width is too low.")

    # Calculate the angle of the object relative to the center of the image
    angle_degrees = ((object_position - image_width / 2) /
                     (image_width / 2)) * (fov_degrees / 2)
    return angle_degrees


def get_speed_from_distance(estimated_distance, max_speed):
    """
    Calculates the speed based on the estimated distance.

    Args:
        estimated_distance (float): The estimated distance.

    Returns:
        float: The speed.
    """
    # Check if the estimated distance is valid
    if estimated_distance < 0:
        raise ValueError("Estimated distance is not a valid distance.")

    MAX_SPEED = max_speed
    MIN_SPEED = 0.05
    REF_DISTANCE = 150.0

    # Calculate the speed based on the estimated distance
    speed = estimated_distance * MAX_SPEED / REF_DISTANCE

    # Check if the speed is below the minimum speed
    if speed < MIN_SPEED:
        speed = MIN_SPEED
    # Check if the speed is above the maximum speed
    elif speed > MAX_SPEED:
        speed = MIN_SPEED

    return speed
