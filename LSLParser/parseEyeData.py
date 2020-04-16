#Joe Snider
#4/20
#
#Parse xdf data from the StreamHTCTobii LSL plugin.
#This is only an example of how to read the data, and it may be adapted to
#  anything that uses LSL.
#Each data sample is:
#   <Time Stamp> <gaze origin x,y,z in Vive coordinates> <gaze direction yaw,pitch,roll in Vive coordinates> <left pupil diameter (mm)> <right pupil mm>
#
#Depends on pyxdf and matplotlib (pip install should work for both)

import pyxdf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pylab as plt

#Sample data taken from Isabelle playing Beat Saber
dat = pyxdf.load_xdf("sub-P001_ses-S001_task-T1[_acq-]_run-004_eeg.xdf")
times = dat[0][0]['time_stamps']
data = dat[0][0]['time_series']

fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.set_title("head position, x,y,z, Vive units")
ax.scatter(data[:,1], data[:,2], data[:,3], c='r', marker='o')

ax2 = fig.add_subplot(222, projection='3d')
ax2.set_title("gaze direction, yaw, pitch roll")
ax2.scatter(data[:,4], data[:,5], data[:,6], c='r', marker='o')

ax3 = fig.add_subplot(223)
ax3.set_title("gaze direction, yaw, pitch, roll (rgb)")
ax3.set_xlabel("Time (s)")
ax3.plot(times, data[:,4], 'r-', times, data[:,5], 'g-', times, data[:,6], 'b-')

ax4 = fig.add_subplot(224)
ax4.set_title("pupil size (mm), left, right (red, blue)")
ax4.set_xlabel("Time (s)")
ax4.plot(times, data[:,7], 'r-', times, data[:,8], 'b-')

plt.show()

