# QR Code Extractor
A Python based QR code extractor that uses OpenCV to detect and extract QR codes in any orientation.
<img src='https://chart.googleapis.com/chart?cht=qr&chl=Hello%20mate!&chs=180x180&choe=UTF-8&chld=L|2'>
<img src='https://chart.googleapis.com/chart?cht=qr&chl=Why%20are%20you&chs=180x180&choe=UTF-8&chld=L|2'>
<img src='https://chart.googleapis.com/chart?cht=qr&chl=looking%20at%20this%3F&chs=180x180&choe=UTF-8&chld=L|2'>
## Features
  - Ability to rapidly detect multiple QR codes in an image or video frame at once
  - Ability to compensate for perspective and simplify codes
  - Compatible with Model 1, Model 2, and SQRC codes
## Important Notes
 - This program *does not* decode QR codes by itself. Decoding must be handled by an outside program (such as ZBar)
 - This code could be much more optimized. Though iterating through squares is not too intensive (as very few contours end up matching the criteria), it could better handle finding the fourth corner and determining the QR code's bounds
 - This code was made as a learning experience, and as such has some major limitations. It is unable to extract QR codes with different colours, distractions or embellishments, and QR codes with more than one alignment locator. It is not meant to be used in a production environment, and is more suited as a learning tool or first step towards making a real QR code reader.
## Methodology - How it works
  ### Step One: Remove noise from sample image
  - Convert original image to greyscale
  - Apply Gaussian blur to reduce noise
  - Apply Canny edge filter to eliminate distractions
  ### Step Two: Narrow down search to only QR code locators
  - Find all remaining contours
  - Filter all contours with approximate vertex count of four
  - Filter all quadrilaterals that are approximately squares and have a certain number of children
  ### Step Three: Locate the locators
  - Loop through all squares
    - Find all squares that are similar in size to the current square
  - If the closest two squares to the current square are similar distances away, estimate that this square is the upper-left locator
  - With the other squares, find the angle from the upper-left vertex to determine the orientation of the QR code
  ### Step Four: Find the alignment pattern square (colloquially called "tiny square" in my code)
  - While searching through squares in previous step, store any squares that are less than half the size of the locator squares
  - After determining locator orientations, calculate the midpoint of the QR code
  - Select from the possible alignment pattern squares the one closest to the midpoint that is also within the bounds of the code itself
  - If alignment pattern is found:
    - Determine fourth corner of the QR code to be a rational distance from the alignment pattern (in a direction opposite of the midpoint)
  - If no alignment pattern is found (smaller QR codes lack this, or the camera may not detect it):
    - Determine edges of the locators that are along the edges of the entire QR code that would intersect to form the fourth corner
    - Find line intersection and determine that point to be the fourth corner
  ### Step Five: Compensate for perspective warping and extract the code
  - For each code, warp the vertices into a square to fix alignment
  - Scale down with cubic interpolation into 29x29 pixel square (change dimensions for different types of codes)
  - Convert to one bit black and white by thresholding the image
  - Return formatted codes in list
 
 ### Hope you find this code helpful, and if you have any questions feel free to contact me!
