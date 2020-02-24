

import sys
import vrep
from time import sleep
from random import randint

debug = False

wheel1 = 2
wheel2 = 2
wheel3 = 2
wheel4 = 2
Turning = False



Speed = 6

print ('Program started')
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP

if clientID != -1:
    print ('Connected to remote API server')

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

    returnCode, front_sensor = vrep.simxGetObjectHandle(clientID, "Proximity_sensor_front",
                                                       vrep.simx_opmode_oneshot_wait)
    returnCode, left_sensor = vrep.simxGetObjectHandle(clientID, "Proximity_sensor_left",
                                                       vrep.simx_opmode_oneshot_wait)
    returnCode, right_sensor = vrep.simxGetObjectHandle(clientID, "Proximity_sensor_right",
                                                       vrep.simx_opmode_oneshot_wait)

    while True:
        returnCode, detectionState1, detectedPoint1, detectedObjectHandle, detectedSurfaceNormalVector = vrep.simxReadProximitySensor(
            clientID, left_sensor, vrep.simx_opmode_streaming)
        left_distance = int(100 * detectedPoint1[2])
        if left_distance <= 0:
            left_distance = 100
        if debug:
            print (detectionState1)
        returnCode, detectionState2, detectedPoint2, detectedObjectHandle, detectedSurfaceNormalVector = vrep.simxReadProximitySensor(
            clientID, right_sensor, vrep.simx_opmode_streaming)
        right_distance = int(100 * detectedPoint2[2])
        if right_distance <= 0:
            right_distance = 100
        if debug:
            print (detectionState2)
        returnCode, detectionState3, detectedPoint3, detectedObjectHandle, detectedSurfaceNormalVector = vrep.simxReadProximitySensor(
            clientID, front_sensor, vrep.simx_opmode_streaming)
        front_distance = int(100 * detectedPoint3[2])
        if front_distance <= 0:
            front_distance = 100
        if debug:
            print (detectionState3)

        print ("Front Reading :{}\n".format(int(detectedPoint3[2] * 100) if detectionState3 else "Nothing in Range"))
        print ("Right Reading :{}\n".format(int(detectedPoint2[2] * 100) if detectionState2 else "Nothing in Range"))
        print ("Left Reading :{}\n".format(int(detectedPoint1[2] * 100) if detectionState1 else "Nothing in Range"))



        if left_distance < 28:
            print ("~~~~~~~~~~~~~~~~~ Obstacle detected Turn right ~~~~~~~~~~~~~~~~~")
            wheel1_speed = Speed / 4
            wheel2_speed = -Speed / 4
            wheel3_speed = Speed / 4
            wheel4_speed = -Speed / 4
        elif right_distance < 28:
            print ("~~~~~~~~~~~~~~~~~ Obstacle detected Turn left ~~~~~~~~~~~~~~~~~")
            wheel1_speed = -Speed / 4
            wheel2_speed = Speed / 4
            wheel3_speed = -Speed / 4
            wheel4_speed = Speed / 4
        elif front_distance < 30:
            print("Move Back...")
            wheel1_speed = -Speed / 4
            wheel2_speed = -Speed / 4
            wheel3_speed = -Speed / 4
            wheel4_speed = -Speed / 4

            vrep.simxSetJointTargetVelocity(clientID, wheel1, wheel1_speed, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(clientID, wheel2, wheel2_speed, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(clientID, wheel3, wheel3_speed, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(clientID, wheel4, wheel4_speed, vrep.simx_opmode_streaming)
            sleep(1)
            if 50 > randint(0, 100):
                print("~~~~~~~~~~~~~~~~~ Random Turn Right ~~~~~~~~~~~~~~~~~")
                wheel1_speed = Speed / 4
                wheel2_speed = -Speed / 4
                wheel3_speed = Speed / 4
                wheel4_speed = -Speed / 4
            else:
                print("~~~~~~~~~~~~~~~~~ Random Turn Left ~~~~~~~~~~~~~~~~~")
                wheel1_speed = -Speed / 4
                wheel2_speed = Speed / 4
                wheel3_speed = -Speed / 4
                wheel4_speed = Speed / 4


        elif front_distance == 100:
            if 25 > randint(0, 100):
                if 30 > randint(0, 100):
                    print("~~~~~~~~~~~~~~~~~ Random Turn Right ~~~~~~~~~~~~~~~~~")
                    wheel1_speed = Speed / 4
                    wheel2_speed = -Speed / 4
                    wheel3_speed = Speed / 4
                    wheel4_speed = -Speed / 4


                elif 30 > randint(0, 100):
                    print("~~~~~~~~~~~~~~~~~ Random Turn Left ~~~~~~~~~~~~~~~~~")
                    wheel1_speed = Speed / 4
                    wheel2_speed = -Speed / 4
                    wheel3_speed = Speed / 4
                    wheel4_speed = -Speed / 4

                else:
                    print("~~~~~~~~~~~~~~~~~ Random Move Forward ~~~~~~~~~~~~~~~~~")
                    wheel1_speed = Speed / 4
                    wheel2_speed = Speed / 4
                    wheel3_speed = Speed / 4
                    wheel4_speed = Speed / 4

            else:
                wheel1_speed = Speed / 4
                wheel2_speed = Speed / 4
                wheel3_speed = Speed / 4
                wheel4_speed = Speed / 4
                # LeftMotorSignal = Speed
                # RightMotorSignal = Speed
        else:
            wheel1_speed = Speed / 4
            wheel2_speed = Speed / 4
            wheel3_speed = Speed / 4
            wheel4_speed = Speed / 4
            # LeftMotorSignal = Speed
            # RightMotorSignal = Speed

        vrep.simxSetJointTargetVelocity(clientID, wheel1, wheel1_speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel2, wheel2_speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel3, wheel3_speed, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, wheel4, wheel4_speed, vrep.simx_opmode_streaming)


        sleep(0.5)
        print ("______________________________________________")
else:
    print ('Failed connecting to remote API server')
    sys.exit("Connection failed")
