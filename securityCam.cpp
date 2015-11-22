#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>

using namespace cv;
using namespace std;

string intToString(int number) {
    stringstream ss;
    ss << number;
    return ss.str();
}

int main(int argc, char* argv[]) {

    bool  recording = false;
    bool startNewRecording = true;
    int videoNumber = 0;

    VideoCapture cap(0); //open video camera number 0, usually default.

    VideoWriter writer;

    if (!cap.isOpened()) { //if camera can not be used, exit program.
        cout << "ERROR INITIALIZING VIDEO CAPTURE" << endl;
        return -1;
    }

    string windowName = "Webcam Feed";
    namedWindow(windowName, CV_WINDOW_AUTOSIZE); //create a window to display webcam feed


    //codec for type of file -> this one is MPEG-4
    int fcc = CV_FOURCC('D', 'I', 'V', '3');

    //frames per sec integer
    int fps = 20;

    //frame size
    Size frameSize(cap.get(CV_CAP_PROP_FRAME_WIDTH), cap.get(CV_CAP_PROP_FRAME_HEIGHT));



    Mat frame; //matrix that stores image.

    while (1) {

        if(startNewRecording) {
            startNewRecording = false;
            recording = true;
            videoNumber++;

            //increments the file by 1.
            string filename = "myVideo.avi" + intToString(videoNumber) + ".avi";
            writer = VideoWriter(filename, fcc, fps, frameSize);


            if(!writer.isOpened()) {
            cout << "ERROR OPENING FILE FOR WRITE" << endl;
            getchar();
            return -1;
            }
        }

        bool bSuccess = cap.read(frame); //read a new frame from feed

        if (!bSuccess) {//test if frame is successfully read
            cout << "ERROR READING FRAME FROM CAMERA FEED" << endl;
            break;
        }

        if(recording) {
            writer.write(frame); //write the frame to the file.
            //Coordinate system starts top left and +x=right, +y=down
            putText(frame,"REC", Point(0,60),2,2,Scalar(0,0,255));
        }

        imshow(windowName, frame); //show the frame in "MyVideo" window.

        //listen for 10ms for a key to be pressed
        switch(waitKey(10)) {
            //esc key pressed
            case 27:
                return 0; //exit program

            //r key pressed
            case 114:
            //toggle recording
                recording = !recording;

                if(recording) {
                    cout <<"Begin Recording" << endl;
                }

                else {
                    cout <<"Recording paused" << endl;
                }

                break;

            //n key pressed
            case 110:
              //start new recording
                startNewRecording = true;

                cout << "New Recording started" << endl;

                break;
        }
    }
    return 0;
}
