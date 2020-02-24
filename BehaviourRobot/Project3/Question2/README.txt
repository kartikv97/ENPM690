# ENPM 690 Robot Learning
@ Author Kartik Venkat


Instructions to run the code:

1.Using Command Prompt:
First run the KV_Vrep_Demonstration_final_Q2.ttt VREP file. The run the following command in command prompt:
python ...PATH...\BehaviourRobot\Project3\Question2\project3_q2.py       // use python3 if using Linux based OS

2.Using PyCharm or any other IDE:

Open KV_Vrep_Demonstration_final_Q2.ttt VREP file and project3_q2 python file and 
Run the VREP file first and then the Python file.



Special Instructions:

-- Install all package dependencies like pynput before running the code.
-- Update pip and all the packages to the latest versions.
-- Make sure you have the following files in your directory:
	1. vrep.py
	2. vrepConst.py
	3. simpleTest.py (or any other example file) 
	4. The appropriate remote API library: "remoteApi.dll" (Windows)(64-bit/32-bit), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)
	5. Go to this path directory to find the remoteApi.dll C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\
-- Change the port number from 19999 to 19997 or vice versa incase the connection to vrep fails.
