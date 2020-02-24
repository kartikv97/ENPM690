# coding: utf-8

# ENPM 690 Robot Learning

# Assignment 3

#@ author: Kartik Venkat


import sys

from pynput.keyboard import Key, Listener

import vrep
from threading import Thread
from time import sleep

flag = False

Speed = 4
# Use multi-threading to print the sensor values in the command window.
def threaded_function():
    while True:
        errorCode, detectionState1, detectedPoint1, detectedObjectHandle, detectedSurfaceNormalVector = vrep.simxReadProximitySensor(
            clientID, front_sensor, vrep.simx_opmode_streaming)
        if flag:
            print (detectionState1)

        print ("Front Sensor Reading :{}\n".format(int(detectedPoint1[2]*100) if detectionState1 else "Nothing in Range"))


        sleep(0.5)
        print ("______________________________________________")


def on_press(event):
    if event == Key.up:
        if flag:
            print ("UP")
        vrep.simxSetJointTargetVelocity(clientID, wheel1, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel2, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel3, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel4, Speed, vrep.simx_opmode_streaming)
        print ("~~~~~~~~~~~~~~~~~ Move Forward ~~~~~~~~~~~~~~~~~")
    elif event == Key.right:
        if flag:
            print ("RIGHT")
        vrep.simxSetJointTargetVelocity(clientID, wheel1, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel2, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel3, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel4, -Speed, vrep.simx_opmode_streaming)
        print ("~~~~~~~~~~~~~~~~~ Turn Right ~~~~~~~~~~~~~~~~~")
    elif event == Key.left:
        if flag:
            print ("LEFT")
        vrep.simxSetJointTargetVelocity(clientID, wheel1, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel2, Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel3, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel4, Speed, vrep.simx_opmode_streaming)
        print ("~~~~~~~~~~~~~~~~~ Turn Left ~~~~~~~~~~~~~~~~~")
    elif event == Key.down:
        if flag:
            print ("DOWN")
        vrep.simxSetJointTargetVelocity(clientID, wheel1, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel2, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel3, -Speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel4, -Speed, vrep.simx_opmode_streaming)
        print ("~~~~~~~~~~~~~~~~~ Move Backward ~~~~~~~~~~~~~~~~~")


def on_release(key):
    if flag:
        print ("{} released".format(key))
    vrep.simxSetJointTargetVelocity(clientID, wheel1, 0, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheel2, 0, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheel3, 0, vrep.simx_opmode_streaming)
    vrep.simxSetJointTargetVelocity(clientID, wheel4, 0, vrep.simx_opmode_streaming)


print ('Setting Up Simulation Environment...')
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP

if clientID != -1:
    print ('Connection Established to remote API server')
    returnCode, wheel1 = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fr', vrep.simx_opmode_blocking);
    print(returnCode)
    print(wheel1)
    returnCode, wheel2 = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fl', vrep.simx_opmode_blocking);
    print(returnCode)
    print(wheel2)
    returnCode, wheel3 = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rr', vrep.simx_opmode_blocking);
    print(returnCode)
    print(wheel3)
    returnCode, wheel4 = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rl', vrep.simx_opmode_blocking);
    print(returnCode)
    print(wheel4)

    returnCode, front_sensor = vrep.simxGetObjectHandle(clientID, "Proximity_sensor",
                                                     vrep.simx_opmode_oneshot_wait)

    thread = Thread(target=threaded_function)
    thread.start()
    #  Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
else:
    print ('Failed to connect to API server')
    sys.exit("Connection failed")
