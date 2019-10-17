# Face-Recognition-System-using-opencv

ABSTRACT :

Face Recognition systems use computer algorithms to pick out specific, distinctive details about a person’s face. These details, such as distance between the eyes or shape of the chin, are then converted into a mathematical representation and compared to data on other faces collected in a face recognition database. The data about a particular face is often called a face template and is distinct from a photograph because it’s designed to only include certain details that can be used to distinguish one face from another.
•	SOFTWARE AND HARDWARE REQUIREMENT:
•	Python 3.3+ or Python 2.7
•	macOS or Linux  or windows
•	OpenCV
•	Pycharm or python IDLE
•	More than 4gb ram
•	Webcam or external camera




•	PLATFORM USED:

•	Pycharm or python IDLE

•	INTRODUCTION:

There are three easy steps to computer coding facial recognition, which are similar to the steps that our brains use for recognizing faces. These steps are:

Data Gathering: Gather face data (face images in this case) of the persons you want to identify.
Train the Recognizer: Feed that face data and respective names of each face to the recognizer so that it can learn.
Recognition: Feed new faces of that people and see if the face recognizer you just trained recognizes them.

•	ALGORITHM:
The LBPH Face Recognizer Process
•	Take a 3×3 window and move it across one image. At each move (each local part of the picture), compare the pixel at the center, with its surrounding pixels. Denote the neighbors with intensity value less than or equal to the center pixel by 1 and the rest by 0.

•	After you read these 0/1 values under the 3×3 window in a clockwise order, you will have a binary pattern like 11100011 that is local to a particular area of the picture. When you finish doing this on the whole image, you will have a list of local binary patterns.
•	
 
•	LBP conversion to binary. Source: López & Ruiz; Local Binary Patterns applied to Face Detection and Recognition.

•	Now, after you get a list of local binary patterns, you convert each one into a decimal number using binary to decimal conversion (as shown in above image) and then you make a histogram of all of those decimal values. A sample histogram looks like this:

 
•	Histogram Sample.

•	In the end, you will have one histogram for each face in the training data set. That means that if there were 100 images in the training data set then LBPH will extract 100 histograms after training and store them for later recognition. Remember, the algorithm also keeps track of which histogram belongs to which person.

  The algorithm is already trained. Each histogram created is used to represent each image from the training dataset. So, given an input image, we perform the steps again for this new image and creates a histogram which represents the image.
•	So to find the image that matches the input image we just need to compare two histograms and return the image with the closest histogram.
•	We can use various approaches to compare the histograms (calculate the distance between two histograms), for example: euclidean distance, chi-square, absolute value, etc. In this example, we can use the Euclidean distance (which is quite known) based on the following formula:
•	So the algorithm output is the ID from the image with the closest histogram. The algorithm should also return the calculated distance, which can be used as a ‘confidence’ measurement. Note: don’t be fooled about the ‘confidence’ name, as lower confidences are better because it means the distance between the two histograms is closer.

•	FUTURE SCOPE
1.	Retail, Marketing, and Advertising
Facial recognition is still in its infancy in retail and marketing, but there are some interesting trails done by big companies.
A way to utilize face recognition technology is by placing cameras in retail outlets. That way it is possible to analyze and improve the customer purchasing process by accessing customer information from their social media profiles and offering customized offers and products.

The American department store Saks Fifth Avenue is already using such a system. Amazon GO stores are reportedly using it as well.
   2. Banking
The banking industry is using facial recognition to both prevent fraud and making online banking safer. HSBC launched a Face ID verification option for their corporate clients in more than 24 countries. The Face ID login is even faster than Touch ID.
3.Security
The security sector is a veteran when it comes to using facial recognition.
Face verification has been used at many country borders ever since the digitized biometric passport was introduced in 2006.
As we’ve mentioned before, police forces are avid users of face recognition technology as well. One of the most memorable accomplishments of this technology was in 2016 when the “man in the hat”, responsible for the Brussels terror attacks, was identified thanks to FBI facial recognition software.
Many high-security facilities, such as government buildings and nuclear plants, implement facial verification technology to check the identities of employees.



•	REFERENCES: 
•	https://www.youtube.com/watch?v=-ZrDjwXZGxI #opencv for face recongniton.
•	LBPH OpenCV: https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#local-binary-patterns-histograms
•	https://www.superdatascience.com/blogs/opencv-face-recognition
•	Deep learning Coursera(Andrew NG)
