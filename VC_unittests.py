import unittest
import random
from  SSLBLACKOUT.vector_calculation import get_object_angle

class TestVectorCalculation(unittest.TestCase):
    def test_get_object_angle(self):
        # Assuming the function takes three parameters: object_position, image_width, fov_degrees
        image_width = random.randint(1,800)
        print(image_width)
        object_position = random.randint(0,image_width)
        print(object_position)
        fov_degrees = random.randint(1,359)
        print(fov_degrees)

        # Call the function with the test parameters
        result = get_object_angle(object_position, image_width, fov_degrees)
        print(result)
        # Check the result - this will depend on what get_object_angle is supposed to do
        # Here we're just checking that it returns a non-negative number
        self.assertTrue(result <= fov_degrees/2 and result >= fov_degrees/-2)
        
    def test_get_object_angle_wrong_parameters(self):
        object_position = 366
        image_width = 200
        fov_degrees = 60
        
        with self.assertRaises(ValueError):
            get_object_angle(object_position,image_width,fov_degrees)
            
        object_position = 150
        fov_degrees = 874
        
        with self.assertRaises(ValueError):
            get_object_angle(object_position,image_width,fov_degrees)
          
        fov_degrees = 40
        image_width = -123
          
            
        
        with self.assertRaises(ValueError):
            get_object_angle(object_position,image_width,fov_degrees)
        

if __name__ == '__main__':
    unittest.main()