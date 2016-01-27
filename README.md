# Project Title

A motion tracker than can turn any webcam into a remote motion tracker. The motion tracker can be control via SMS, currently with START and STOP commands. The user is also notified when motion is detected via SMS and a video copy of the motion is stored in the user's Dropbox.The application was intentially created to work on the Raspberry Pi, however it can work on any linux based computer that has OpenCV installed. Various filters are used to limit motion detection to only large movements, lowering the possibility of false alerts.

## Prerequisities

To properly run RemoteSecurity, you must have the following availale:
* OpenCV
* Linux Distro
* Camera
* Flask
* ngrok
* Python
* Twilio

## Deployment

To run the server portion of the application, you must first create a public domain for the Twilio API to work with, run:
```
./ngrok http 5000
```
launch the RemoteSecurity Application by running: 
```
python run
```

## Built With

* OpenCV - Library for image processing
* Flask - Framework for server
* Twilio - SMS API that gives user control over the camera
* ngrok - localizes a port for public access

## Notes

Dropbox integration will be coming soon.
