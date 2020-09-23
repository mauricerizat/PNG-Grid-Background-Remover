# PNG Grid Background Remover
This simple application removes the gray-and-white grid backgrounds from non-transparent image files, converting them into transparent .png images.

## EXAMPLE RESULT:

Before | After
-------|------
![butterfly](https://user-images.githubusercontent.com/49680882/94039893-eb957480-fde5-11ea-959c-a9d7c06ac4d5.jpg) | ![butterflyTransparent](https://user-images.githubusercontent.com/49680882/94039894-eb957480-fde5-11ea-9fb6-22831a21fa71.png)

## USE:
Step | Image
-----|-----
Start the program by running the given executable (.exe) file. The following home screen should be displayed. To select an image, click the **Select File** button | ![1  home](https://user-images.githubusercontent.com/49680882/94039873-e59f9380-fde5-11ea-8a0a-e024064bfc75.png)
The file selection window should appear. The program can only accept images file formats. If non-image files are selected, an error will occur. |  ![2  selection](https://user-images.githubusercontent.com/49680882/94039879-e7695700-fde5-11ea-9efe-38242e5ef4f8.png)
Once selected, a preview of the selected image should be displayed on screen. Now select the tolerance level for the grid. A higher tolerance will allow for more shades of white and gray to exist while a lower tolerance will remove all shades of white and gray in the image. | ![3  tolerance select](https://user-images.githubusercontent.com/49680882/94039881-e801ed80-fde5-11ea-93b5-35c7f10f6ca4.png)
Now name your output file. The default value for the output file name is "defaultOutput". You do not need to suffix an extension for the file. The output image will be of .png format and will be located in the same folder as the selected input file. | ![4  named](https://user-images.githubusercontent.com/49680882/94039883-e89a8400-fde5-11ea-9af6-30c01bb50d26.png)
Now click the **Remove Grid Background** button. This should initiate the grid removal process | ![5  select remove grid](https://user-images.githubusercontent.com/49680882/94039885-e9331a80-fde5-11ea-8598-63bd0b36fc16.png)
During the grid removal process, the **Remove Grid Background** button will say **PROCESSING...** and the program window will remain disabled. | ![6  processing](https://user-images.githubusercontent.com/49680882/94039887-e9cbb100-fde5-11ea-8228-dd5a3ced32e6.PNG)
Once the grid removal process is complete, an alert will be displayed | ![7  success](https://user-images.githubusercontent.com/49680882/94039890-ea644780-fde5-11ea-89b0-55229d16bed7.PNG)
Your output image will be of .png format and will be located in the same folder as the input file. | ![9  directory](https://user-images.githubusercontent.com/49680882/94039892-eafcde00-fde5-11ea-9ac7-5f799c217905.png)

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
- Use Multicore GPU processing to speed up processing for large images


Contact me at *mauricerizat@gmail.com* to report bugs
