# Sail Number Recognition

## Introduction 
During a race for sailing, windsurfing or any competitive water sport racing, everytime when a boat/board passes a buoy/mark, a start line or a finish line, committees will need to mark the sail number down. ([Here's a windsurfing race from Youtube. For real, it is so exciting!](https://www.youtube.com/watch?v=hmafoMOBWkU)) In a large size race where there will be up to a hundred of racers, it becomes really difficult for the committees to write down the numbers. 

This project tends to use Optical Character Recognition or OCR to automatically capture sail number. The goal of the tool is to reduce human error or even reduce the number of committees needed, which in turn reduces the need of race training. 

In this project, I will be focusing on windsurfing, just because that is the sport I have been playing for the longest time and I want to develop this tool to help the local community. 

### Goal of the Project 
1. Create an algorithm to recognize sail number when supplied with an image 
1. Real-time classification with video 
1. Create a mobile app to deploy the algorithm

## Method

* Optain lots of images of sails with sail number on it from online resources (google obviously...)
* Create OCR algorithm that can recognize sail number (found a tool called PyTesseract)
* Train the algorithm 
* Test the algorithm 

### Current Progress! 
* Learned how to use 1) Pytesserat for OCR, 2) openCV for image processing
* Main script (SailNumberDetection.py) currently can detect where the sail number is and crop the image out. (if the image doesn't have too much noise and the sail number is not too distored...)

![Alt Text](https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif)

