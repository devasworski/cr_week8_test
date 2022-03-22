Alexander Sworski
210456914

Step 1)
To run this project, the project folder has to be placed within a ROS workspace such as catkin_ws. Afterwards the following commands have to be executed within the terminal:

    1. cd ~/catkin_ws/
    2. catkin_make
    3. source devel/setup.bash

Step 2)
After running the following commands the project has been build and can be started. For this, the roscose has to be started first. To start the roscore, a new terminal window needs to be opened and the follwing command needs to be executed. This terminal window needs to stay active in the background while executing this project.

    1. roscore

Step 3)
After executing the previous steps, the project can be started. For this we switch to the first terminal window used in Step 1 and execute the following command start the project using the launch file:

    1. roslaunch cr_week8_test human_robot_interaction.launch

The launch file will start the 4 ros nodes and will display the robots assessment of the scene and the scene id within the terminal window.