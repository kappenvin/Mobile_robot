
# mobile_robot

## to run the robot with an xbox controller 

### on the home pc 

ros2 launch teleop_twist_joy teleop-launch.py

ros2 param set /teleop_twist_joy_node enable_button 1 if set to 0 

Afterwards you have to press B if in the upwards command set to 0 then press A an move in the direction

you can see the output in the terminal with 
ros2 topic echo /cmd_vel

### on  the raspberry_pi

ros2 run vision_rpi_bot cmdVel_to_pwm_node