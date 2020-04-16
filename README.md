# StreamHTCTobii
Stream data over LSL from an HTC Vive Pro with eye tracking. 

## Usage

The project is mostly a test scene for the StreamEyes asset. Before starting you should set up eye tracking on the Vive before using this: calibrate and make sure the eye data are streaming.
At startup StreamEyes will connect to the eye tracking and start an [LSL stream](https://github.com/sccn/labstreaminglayer). Most of the action is in the Update loop and it as examples of how to check the status, frame rate, and so on.
It sends:
<Time Stamp> <gaze origin x,y,z in Vive coordinates> <gaze direction yaw,pitch,roll in Vive coordinates> <left pupil diameter (mm)> <right pupil mm>

![sample data](/LSLParser/Figure_1.png)Sample output from someone playing Beat Saber while the data was being recorded.

Note that you *should* be able to run this as a separate plugin from your other code: run the executable in Build.7z in parallel to any other game.
