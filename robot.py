#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib as wp
import rev
import wpilib.drive as wpd

class MyRobot(wp.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # defines the camera function
        wp.CameraServer.launch()

        self.configleft = rev.SparkMaxConfig().follow(2)
        self.configright = rev.SparkMaxConfig().follow(5)

        # defines the drivetrain
        self.frontLeftDrive = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushed)
        self.backLeftDrive = rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushed)
        self.backRightDrive = rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushed)
        self.frontRightDrive = rev.SparkMax(5, rev.SparkLowLevel.MotorType.kBrushed)

        self.backLeftDrive.configure(self.configleft, rev.SparkBase.ResetMode.kResetSafeParameters, rev.SparkBase.PersistMode.kNoPersistParameters)
        self.backRightDrive.configure(self.configright, rev.SparkBase.ResetMode.kResetSafeParameters, rev.SparkBase.PersistMode.kNoPersistParameters)

        self.robotDrive = wpd.DifferentialDrive(
            self.frontLeftDrive, self.frontRightDrive
        )

        self.controller = wp.XboxController(0)
        self.timer = wp.Timer()

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        self.backLeftDrive.setInverted(True)
        self.frontLeftDrive.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()  # Stop robot

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getLeftX()
        )

    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wp.run(MyRobot)
