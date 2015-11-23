#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>
#include <time.h>

using namespace std;
using namespace cv;

//our sensitivity value to be used in the absdiff() function
//for higher sensitivity, use a lower value
const static int SENSITIVITY_VALUE = 40;
//size of blur used to smooth the intensity image output from absdiff() function
const static int BLUR_SIZE = 10;
//these two can be toggled by pressing 'd' or 't'
bool debugMode;
bool trackingEnabled;

//int to string helper function
string intToString(int number){

	//this function has a number input and string output
	std::stringstream ss;
	ss << number;
	return ss.str();
}

string getDateTime(){
	//get the system time
	time_t rawtime;
  struct tm * timeinfo;
  char buffer [50];
  time (&rawtime);
  timeinfo = localtime (&rawtime);
  strftime (buffer,50,"%B %d %G - %r",timeinfo);

	stringstream stream;
	stream << buffer;

	return stream.str();
}

string getFileDateTime(){
	//get the system time
	time_t rawtime;
  struct tm * timeinfo;
  char buffer [30];
  time (&rawtime);
  timeinfo = localtime (&rawtime);
  strftime (buffer,30,"%m_%d_%G_%H_%M_%S",timeinfo);

	stringstream stream;
	stream << buffer;

	return stream.str();
}

bool detectMotion(Mat thresholdImage, Mat &cameraFeed){
	//create motionDetected variable.
	bool motionDetected = false;
	//create temp Mat for threshold image
	Mat temp;
	thresholdImage.copyTo(temp);
	//these two vectors needed for output of findContours
	vector< vector<Point> > contours;
	vector<Vec4i> hierarchy;
	//find contours of filtered image using openCV findContours function
	//findContours(temp,contours,hierarchy,CV_RETR_CCOMP,CV_CHAIN_APPROX_SIMPLE );// retrieves all contours
	findContours(temp,contours,hierarchy,CV_RETR_EXTERNAL,CV_CHAIN_APPROX_SIMPLE );// retrieves external contours

	//if contours vector is not empty, we have found some objects
	//we can simply say that if the vector is not empty, motion in the video feed has been detected.
	if(contours.size()>0)motionDetected=true;
	else motionDetected = false;

	return motionDetected;

}
int main(){
	//set recording and startNewRecording initially to false.
	bool recording = false;
	bool startNewRecording = false;
	int inc=0;
	bool firstRun = true;
	//if motion is detected in the video feed, we will know to start recording.
	bool motionDetected = false;

	//pause and resume code (if needed)
	bool pause = false;
	//set debug mode and trackingenabled initially to false
	//these can be toggled using 'd' and 't'
	debugMode = false;
	trackingEnabled = true;
	//set up the matrices that we will need
	//the two frames we will be comparing
	Mat frame1,frame2;
	//their grayscale images (needed for absdiff() function)
	Mat grayImage1,grayImage2;
	//resulting difference image
	Mat differenceImage;
	//thresholded difference image (for use in findContours() function)
	Mat thresholdImage;
	//video capture object.
	VideoCapture capture;
	capture.open(0);
	VideoWriter oVideoWriter;//create videoWriter object, not initialized yet
	double dWidth = capture.get(CV_CAP_PROP_FRAME_WIDTH); //get the width of frames of the video
	double dHeight = capture.get(CV_CAP_PROP_FRAME_HEIGHT); //get the height of frames of the video
	//set framesize for use with videoWriter
	Size frameSize(static_cast<int>(dWidth), static_cast<int>(dHeight));

	if(!capture.isOpened()){
		cout<<"ERROR ACQUIRING VIDEO FEED\n";
		getchar();
		return -1;
	}
	while(1){
		//read first frame
		capture.read(frame1);
		//convert frame1 to gray scale for frame differencing
		cv::cvtColor(frame1,grayImage1,COLOR_BGR2GRAY);
		//copy second frame
		capture.read(frame2);
		//convert frame2 to gray scale for frame differencing
		cv::cvtColor(frame2,grayImage2,COLOR_BGR2GRAY);
		//perform frame differencing with the sequential images. This will output an "intensity image"
		//do not confuse this with a threshold image, we will need to perform thresholding afterwards.
		cv::absdiff(grayImage1,grayImage2,differenceImage);
		//threshold intensity image at a given sensitivity value
		cv::threshold(differenceImage,thresholdImage,SENSITIVITY_VALUE,255,THRESH_BINARY);
		if(debugMode==true){
			//show the difference image and threshold image
			cv::imshow("Difference Image",differenceImage);
			cv::imshow("Threshold Image", thresholdImage);
		}else{
			//if not in debug mode, destroy the windows so we don't see them anymore
			cv::destroyWindow("Difference Image");
			cv::destroyWindow("Threshold Image");
		}
		//blur the image to get rid of the noise. This will output an intensity image
		cv::blur(thresholdImage,thresholdImage,cv::Size(BLUR_SIZE,BLUR_SIZE));
		//threshold again to obtain binary image from blur output
		cv::threshold(thresholdImage,thresholdImage,SENSITIVITY_VALUE,255,THRESH_BINARY);
		if(debugMode==true){
			//show the threshold image after it's been "blurred"

			imshow("Final Threshold Image",thresholdImage);

		}
		else {
			//if not in debug mode, destroy the windows so we don't see them anymore
			cv::destroyWindow("Final Threshold Image");
		}

		//if tracking enabled, search for Motion
		if(trackingEnabled){

			//check for motion in the video feed
			//the detectMotion function will return true if motion is detected, else it will return false.
			//set motionDetected boolean to the returned value.
			motionDetected = detectMotion(thresholdImage,frame1);

		}else{
			//reset our variables if tracking is disabled
			motionDetected = false;

		}

////////////**STEP 1**//////////////////////////////////////////////////////////////////////////////////////////////////////////////
		//draw time stamp to video in bottom left corner. We draw it before we write so that it is written on the video file.
		string dateTime = getDateTime();
		rectangle(frame1, Rect(0,465,290,15), Scalar(255,255,255), -1);
		putText(frame1, dateTime, Point(0,480), 1, 1, Scalar(0,0,0),2);
		//if we're in recording mode, write to file
		if(recording){

			//check if it's our first time running the program so that we don't create a new video file over and over again.
			//we use the same boolean check to create a new recording if we want.
			if(firstRun == true || startNewRecording == true){

//////////**STEP 3**///////////////////////////////////////////////////////////////////////////////////////////////////////////////
				//Create a unique filename for each video based on the date and time the recording has started
				//string videoFileName = "SecurityRecording"+intToString(inc)+".avi";
				string videoFileName = getFileDateTime() + ".avi";

				cout << "File has been opened for writing: " << videoFileName<<endl;

				cout << "Frame Size = " << dWidth << "x" << dHeight << endl;

				oVideoWriter  = VideoWriter(videoFileName, CV_FOURCC('D', 'I', 'V', '3'),10, frameSize, true);

				if ( !oVideoWriter.isOpened() )
				{
					cout << "ERROR: Failed to initialize video writing" << endl;
					getchar();
					return -1;
				}
				//reset our variables to false.
				firstRun = false;
				startNewRecording = false;
			}

			oVideoWriter.write(frame1);
			//show "REC" in top left corner in red
			//be sure to do this AFTER you write to the file so that "REC" doesn't show up on the recorded video file.
			//Cut and paste the following line above "oVideoWriter.write(frame1)" to see what I'm talking about.
			putText(frame1,"REC",Point(0,60),2,2,Scalar(0,0,255),2);
		}

		//check if motion is detected in the video feed.
		if(motionDetected){
			//show "MOTION DETECTED" in bottom left corner in green
			putText(frame1,"MOTION DETECTED",cv::Point(0,420),2,2,cv::Scalar(0,255,0));
			recording = true;
		}

		else {
			recording = false;
		}
		//show our captured frame
		imshow("Frame1",frame1);

		//check to see if a button has been pressed.
		//the 30ms delay is necessary for proper operation of this program
		//if removed, frames will not have enough time to referesh and a blank image will appear.
		switch(waitKey(30)){

		case 27: //'esc' key has been pressed, exit program.
			return 0;
		case 116: //'t' has been pressed. this will toggle tracking (disabled for security cam)
			/*trackingEnabled = !trackingEnabled;
			if(trackingEnabled == false) cout<<"Tracking disabled."<<endl;
			else cout<<"Tracking enabled."<<endl;*/
			break;
		case 100: //'d' has been pressed. this will debug mode
			debugMode = !debugMode;
			if(debugMode == false) cout<<"Debug mode disabled."<<endl;
			else cout<<"Debug mode enabled."<<endl;
			break;
		case 112: //'p' has been pressed. this will pause/resume the code.
			pause = !pause;
			if(pause == true){ cout<<"Code paused, press 'p' again to resume"<<endl;
			while (pause == true){
				//stay in this loop until
				switch (waitKey()){
					//a switch statement inside a switch statement? Mind blown.
				case 112:
					//change pause back to false
					pause = false;
					cout<<"Code Resumed"<<endl;
					break;
				}
			}
			}
		case 114:
			//'r' has been pressed.
			//toggle recording mode
			recording =!recording;

			if (!recording)cout << "Recording Stopped" << endl;

			else cout << "Recording Started" << endl;

			break;

		case 110:
			//'n' has been pressed
			//start new video file
			startNewRecording = true;
			recording = true;
			cout << "New Recording Started" << endl;
			//increment video file name
			inc+=1;
			break;
		}
	}
	return 0;
}
