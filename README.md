# FACE RECOGNITION BASED SECURITY CAMERA AND DOOR UNLOCK SYSTEM

### ABSTRACT
In today's era, we are facing many security challenges on every level. We must use current technologies to solve these issues in order to overcome them. As a result, we came up with the idea of a security camera and door unlocking system. The security camera and door unlock system is implemented using Internet of Things (IoT) technology. The main goal is to secure our home by using Python OpenCV face recognition on a Raspberry Pi 3. When someone approaches the door, the camera catches their face, and the face recognition system running on the Raspberry Pi 3 recognises the person's face, compares it to the faces present in the database, and sends an email to the administrator stating that "someone is waiting at the door". The administrator can then use the door unlock system web app to unlock the door. We'll be using face recognition methods from the OpenCV Python package.

### INTRODUCTION
The Internet of Things, or IoT, is a cutting edge technology that allows us to control hardware objects over the internet. In addition, security is a major worry in today's world. So, utilising a face recognition-based Security Camera and Door Unlock System, we came up with the notion of automating door unlocking. The system is constantly checking to see if somebody is standing in front of the door. This technology is quite beneficial since it alerts the administrator when someone approaches the door. Admins can also use the flask web app to open the door by clicking the 'open door' button.

### METHODOLOGY
The Raspberry Pi 3 (a pocket sized single board computer) is used to perform face recognition and door unlocking in this project. To capture live-streaming, a Raspberry Pi Camera or USB Camera is used, and a Solenoid Door Lock is used to lock and unlock the door. A relay module is used to trigger the solenoid door lock, and the solenoid door lock is powered by a 12 Volt Power Supply. There will be a web application and a flask server that will monitor who is at the entrance, and we will be able to control the door lock from a different location. The solenoid lock is connected to a Raspberry Pi 3 that can be controlled remotely. We have used python's face-recognition model for face recognition, which is built with deep learning technology and has 99.32 percent accuracy, OpenCV - Python module for comparing faces from images stored in the database, The MySQL Database to store admin details, The socket's module in Python was used to send video stream data from the Raspberry Pi 3 to the Flask web app, as well as a signal from the web app to the Raspberry Pi 3 to unlock the door lock.
When someone comes to the door, the camera recognises their face, compares it to the images in the database, and sends an email to the administrator stating that "someone is waiting at the door." The administrator can then use the door unlock system web app to open the door. When the administrator presses the button on the app, the signal is sent to the Raspberry Pi, which triggers the relay module, which switches on the solenoid lock's power supply and unlocks it. The admin can delete, modify, and add new user details to the database using the flask web app, as well as monitor live stream video of the security camera and open the door for the user to enter.

![image](https://user-images.githubusercontent.com/68019573/223484832-bcad500a-8be9-4d46-b72d-a5907ccdeaca.png)
#### Figure 4.6 Flow Chart of the System

![image](https://user-images.githubusercontent.com/68019573/223483078-3226c592-2bfd-4a09-8889-fe5a995568fc.png)
#### Figure 2: System Design

### ANALYSIS AND CODES
#### • Python web app
It's a user-friendly UI built using the Flask web framework that helps in controlling Raspberry Pi and accessing user data, among several other things.

#### • Login
Only authorised admins have access to the dashboard, which is why the Login form is needed.

#### • Signup
The Signup form is used for the registration of the new admin.

#### • Admin Dashboard
To access this page, the administrator must first log in. From here, the administrator can monitor users, add new users, modify the details of current users, and delete users. Additionally, the administrator can open the door automatically and view live stream video from the security camera.

#### • MySQL Server
MySQL is a free and open-source database used to store data. The MySQL Server is used to store user data and face images, which is used to give access to open the door.
