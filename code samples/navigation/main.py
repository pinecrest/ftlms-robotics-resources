#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

r_motor = Motor(Port.C)
l_motor = Motor(Port.B)
# measure these for each robot - this could change based on the robot design
wheel_diameter = 56
axle_track = 114

driver = DriveBase(l_motor, r_motor, wheel_diameter, axle_track) 

def drive_distance(distance_mm):
    speed = 300.0 # mm per second
    ttd = distance_mm / speed * 1000
    driver.drive(speed, 0)
    wait(ttd)
    driver.stop(Stop.BRAKE)

drive_distance(1250)