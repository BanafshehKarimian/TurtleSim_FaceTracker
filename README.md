# TurtleSim_FaceTracker
In this project we want to make th eturtle in turtlesim move as our face moves and control it with our face. In order to do so, we define a new masage coordinate_msg that contains the x and y coordinate of a face you can check it using:
```console
rosmsg show package_name/coordinate_msg
```
The sendfacetracker.py file is a publisher which finds the face using haarcascade and publishes the middle point of the found face using coordinate_msg (you can test it using:
```console
rosrun package_name sendfacetracker.py
rostopic echo /coordinate
```
<br /> Next the subscriber node is coded in calculaternode.py which recieves the coordinate of the face and the position of the turtle. It then publishes the speed the turtle need to move through calculating the distance of pose to its required location corresponding to the face.
<br />You can launch the project using:
```console
roslaucn package_name pckg_lauch.launch
```
<br />The followings are the rqt_graph and a sample movement of the turtle.<br />
![](https://github.com/BanafshehKarimian/TurtleSim_FaceTracker/blob/main/result.png)<br />
![](https://github.com/BanafshehKarimian/TurtleSim_FaceTracker/blob/main/graph.PNG)<br />
