<img src="https://people.bath.ac.uk/mtc47/img/collaborators/QM_Logo.png" height=100>

## Cognitive Robotocs (Lab 8): 
# Social human-robot simulation

Module Code: **ECS794P** 

Module Leader: **Lorenzo Jamone**

Student Name: **Alexander Sworski**

Student ID: **210456914**

Semester: **2**

Submission Date: **22th March 2022**

#### Final Grade: ??

## Task
The objective of this Mid-term Test (10% of your final exam mark) is to create a ROS package that simulates a simple computational model of social human-robot interaction.

## Manual

### SETUP

#### Step 1:
To run this project, the project folder has to be placed within a ROS workspace such as catkin_ws.
Afterwards the following commands have to be executed within the terminal:

1. `cd ~/catkin_ws/`
2. `catkin_make`
3. `source devel/setup.bash`

#### Step 2:
After running the following commands the project has been build and can be started. For this, the roscose has to be started first.
To start the roscore, a new terminal window needs to be opened and the follwing command needs to be executed. This terminal window needs to stay active in the background while executing this project.

1. `roscore`

#### Step 3:
**After** executing the previous steps, the project can be started. For this we switch to the first terminal window used in Step 1 and execute the following command start the project using the launch file:

1. `roslaunch cr_week8_test human_robot_interaction.launch`

The launch file will start the 4 ros nodes and will display the robots assessment of the scene and the scene id within the terminal window.

### DESCRIPTION
Consider a social humanoid robot sitting at a table in front of a human child. At each interaction, a different colored toy is placed on the table, and the robot should express one emotion, which depends on both the perceived object properties and the perceived child behavior. This can be modeled with a Bayesian Network. The robot can perceive the size of the object (O), and classify it as either: small, big (they are all equally likely to happen). The robot can perceive human facial expressions (HE), and classify them as either: happy, sad, neutral (they are all equally likely to happen). The robot can perceive human head and eyes movements (actions, HA), and classify them as either: looking at the robot face, looking at the colored toy, looking away (they are all equally likely to happen). The robot face can express three possible emotions (RE): happy, sad, neutral. Note that, during an interaction, the robot might not have access to all the variables (object size, human expression, human action), due to e.g. absence of one of the stimuli or failure of a sensor, but still the robot has to decide what emotion expression is the most likely to be appropriate.

### Knows Issues:
1. The `robot_expression_prediction` service does interrupt after one serice request, leaving the project to show only the robot interpretation of the first scenario.
2. The scenario with the ID 1 is not listed to by the subscribers, therfore the first scenario processed and interpreted by the robot has the ID 2.
