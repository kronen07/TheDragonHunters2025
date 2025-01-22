#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib as wp
import rev


class MyRobot(wp.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # defines the camera function
        wp.CameraServer.launch()
        self.motor: rev.SparkMax = rev.SparkMax(2, rev.SparkBase.MotorType.kBrushed)

        self.controller = wp.XboxController(0)
        self.timer = wp.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""


    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        self.motor.set(self.controller.getLeftX)

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        

    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wp.run(MyRobot)
