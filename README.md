usma_remote_interface
=====================
1. Install all dependencies (assuming ROS Kinetic).
  * `sudo apt-get install ros-kinetic-rosbridge-server`
  * `sudo apt-get install ros-kinetic-web-video-server`
  * `sudo apt-get install ros-kinetic-usb-cam`
 
2. Clone the usma_remote_interface ros package into your catkin workspace src folder.
  * `cd ~/catkin_ws/src`
  * `git clone https://github.com/westpoint-robotics/usma_remote_interface.git usma_remote_interface`
  
3. Run the setup script.
  * `cd ~/catkin_ws/src/usma_remote_interface/scripts`
  * `./usma_remote_interface_setup.sh`

4. Edit the master.launch argument for the correct video input.
  * `cd ~/catkin_ws/src/usma_remote_interface/launch`
  * `ls /dev/video*` (to see available video devices)
  * `gedit remote.launch` (or your preferred editor)
  * Change the video device. Internal webcams will typically be video0, an external webcam could be video1.
    * `<arg name="video_device" default="/dev/video1" />`

5. Edit the javascript config.
  * `roscd usma_remote_interface/webpage`
  * `gedit config.js` (or your preferred editor)
  * Edit the file to reflect desired topics and IPs

6. Launch remote.launch.
  * `roslaunch usma_remote_interface remote.launch`

7. Go to a web browser and enter in the IP address for the computer.
  * url:   \<ip_address_server\>
  * example:   localhost
