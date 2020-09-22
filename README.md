# PNG-Grid-Background-Remover
This simple application removes the gray-and-white grid backgrounds from non-transparent image files, converting them into .png images.

## USE: 
Simply run the exe file, select an image, the tolerance level, make an output file name and click the "Remove Background" button.

## WORKING:
The program is very simple. It is made with python and the GUI is made with the help of tkinter.

How it removes grids is it checks every pixel's RGB values and see if it's range is within "tolerance-percent" of either (255, 255, 255) (white) or (204, 204, 204) (gray).

Therefore, if tolerance is 30% the check for each channel of each pixel is: 

**.7\*255 < pixel < 1.3\*255** and **.7\*204 < pixel < 1.3\*204**. 

If this is the case, the pixel is made transparent by changing it's alpha to zero. If not, the pixel is rendered as original.

## Desired future features:
- Change values of colors to remove i.e. accomodate for when grid values aren't gray-and-white
- Select area within which to not remove white and gray pixels - This is important because the program removes all white and gray pixels which may not be desirable in many cases.
- Modern looking GUI
- Progress bar
