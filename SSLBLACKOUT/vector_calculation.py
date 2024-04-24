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


def get_object_angle(object_position, image_width, fov_degrees):
    if(object_position < 0 or object_position >= image_width ):
        raise ValueError("object position is out of bounds of cam resolution.")
    if(fov_degrees > 360 or fov_degrees <= 0):
        raise ValueError("camera FOV is too low or too high.")
    if(image_width <= 0):
        raise ValueError("image_width_is_too_low")
        
    # Calculate the angle of the ball relative to the center of the image
    angle_degrees = ((object_position - image_width / 2) /
                     (image_width / 2)) * (fov_degrees / 2)
    return angle_degrees

def get_speed_from_distance(estimated_distance):
    if(estimated_distance < 0):
        raise ValueError("Estimated distance in not a valid distance.")
    MAX_SPEED = 3.0
    MIN_SPEED = 0.05
    speed = 0.0
    REF_DISTANCE = 150.0
    

    speed = estimated_distance*MAX_SPEED/REF_DISTANCE

    if(speed < MIN_SPEED):
        speed = MIN_SPEED
    elif(speed > MAX_SPEED):
        speed = MIN_SPEED
        
    return speed

        

    
    