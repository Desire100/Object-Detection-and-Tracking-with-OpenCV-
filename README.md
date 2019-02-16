# Object-Detection-and-Tracking-with-OpenCV-

# Goals
This repository will help you to understand a variety of object detection and tracking methods with help of opencv which is open source computer vison library.

## Template Matching
 Simply looking for an exact copy of an image in another image.
 Template matching is the simplest form of object detection. It simply scans a larger image for a  provided template by sliding the template target image across the larfer image.
 
## Corner Detection 
  Looking for corners to find general edges of objects.
  When thinking about corner detection in computer vision, we should ask ourselvesL What is a corner?
  A corner is a point whose local neighborhood stands in two dominant and different edge directions also a corner can be interpreted as   the   junction of two edges, where an edge is a sudden change in image brightness. 
  
  
  there are various corner detection algorithms:
  ### Harris Corner Detection
   It can be detected by looking for significant change in all directions
   
  ### Shi-Tomasi Corner Detection 
   Made a small modification to the Harris Corner Detector which ended up with better results. 
   Shi-Tomasi Corner Detector & Good Features to Track Paper
[Link to Paper](http://www.ai.mit.edu/courses/6.891/handouts/shi94good.pdf)
#### Good Feature To Track a paper 
Function Parameters
image Input 8-bit or floating-point 32-bit, single-channel image.
corners Output vector of detected corners.
maxCorners Maximum number of corners to return. If there are more corners than are found,the strongest of them is returned. maxCorners <= 0 implies that no limit on the maximum is set and all detected corners are returned.
qualityLevel Parameter characterizing the minimal accepted quality of image corners. The parameter value is multiplied by the best corner quality measure, which is the minimal eigenvalue (see #cornerMinEigenVal ) or the Harris function response (see #cornerHarris ). The corners with the quality measure less than the product are rejected. For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality measure less than 15 are rejected.
  
## Grid Detection 
Combinaing both concepts to find grids in images* useful for applications)

## Contour Detection 
Allows us to detect foreground vs background images, also allows for detection of external vs internal countours (e.g. grabbing the eyes and smile from a cartoon smile face).

## Feature Matching
More advances methods of detecting matching objects in another image, even if the target image is not shown exactly the same in the image we are searching.

## Watershed Algorithm
Advanced a;gorithm that allows us to segment images into foreground and background. also allows us to manually set seeds to choose segments of an image.

## Facial and Eye Detection
we'll use Haar Cascades to detect faces in images, not this not yet facial recognition.

 

 
