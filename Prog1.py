# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK's API
from robodk import *      # Math toolbox for robots

# Start the RoboDK API:
RDK = Robolink()

# Get the robot item by name:
robot = RDK.Item('UR3', ITEM_TYPE_ROBOT)

# Get the reference target by name:
R = 100

for i in range(2):
    target = RDK.Item('Target %s' % (i+1))
    target_pose = target.Pose()
    xyz_ref = target_pose.Pos()

    # Move the robot to the reference point:
    robot.MoveJ(target)
    # Draw a hexagon around the reference target:
    for i in range(7):
        ang = i * 2 * pi / 6 # ang = 0, 60, 120, ..., 360

        # Calculate the new position around the reference:
        x = xyz_ref[0] + R * cos(ang) # new X coordinate
        y = xyz_ref[1] + R * sin(ang) # new Y coordinate
        z = xyz_ref[2]                # new Z coordinate
        target_pose.setPos([x,y,z])

        # Move to the new target:
        robot.MoveL(target_pose)

    # Trigger a program call at the end of the movement
    # robot.RunCode('Program_Done')

# Move back to the reference target:
robot.MoveL(target)
