 #!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import (
    Port,
    Stop,
    Direction,
    Button,
    Color,
    SoundFile,
    ImageFile,
    Align,
)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

r_motor = Motor(Port.C)
l_motor = Motor(Port.B)

# Defaulted to basic EV3 robot measurements.
# measure these for each robot - this could change based on the robot design
wheel_diameter = 56
axle_track = 114

driver = DriveBase(l_motor, r_motor, wheel_diameter, axle_track)


def drive_distance(distance_mm, speed_mm_s=300):
    """
    This function uses the DriveBase object to move the robot 
    forward in a straight line for a given distance in millimeters. 
    The speed is currently fixed at 300 mm per second.
    This does NOT use the gyro or any sensors other than what is 
    included in DriveBase.

    We've also added ramp parameters to smoothly increase the motor speed
    and prevent jerky starts.

    params:
    distance_mm - the distance to travel in millimeters

    """
    ramp_interval = 1 # this is the time in seconds to ramp up
    ramp_steps = 10

    for i in range(ramp_steps):
        driver.drive(speed_mm_s / (i + 1)) 
        wait(ramp_interval * 1000 / ramp_steps)
    distance_mm -= (speed_mm_s * ramp_interval / 2)
    if distance_mm <= 0:
        driver.stop(Stop.BRAKE)
        return
    ttd = distance_mm / speed_mm_s * 1000
    driver.drive(speed_mm_s, 0)
    wait(ttd)
    driver.stop(Stop.BRAKE)

def turn_angle(angle_deg, speed_deg_s=180) 
    pass

if __name__ == "__main__":
    drive_distance(1250)
