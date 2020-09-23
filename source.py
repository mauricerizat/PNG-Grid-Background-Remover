"""Imports"""
import os

from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Progressbar
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

"""Global Variables"""
filename = "none" #Default filename. This string "none" will be used to check no file selected
photo1 = ImageTk.PhotoImage #stores displayed image
tolerancePercent = 50 #Tolerance value. Default is 50
outputFile = "defaultOutput" #Stores full part of output file

#
def resource_path(relative_path): 
    """This is primarily for when exe is created. It returns a usable path for the given relative path"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def fileSelect():
    """
    This function performs file selection
    Called by press of selectFileButton
    """
    global filename, photo1 #Global variables to use
    
    try:
        filename = askopenfilename() #File input  
        
        #Change display image
        imageShow = Image.open(filename) 
        imageShow = imageShow.resize((300, 250), Image.ANTIALIAS) 
        photo1 = ImageTk.PhotoImage(imageShow)     
        photoLabel.config(image=photo1)
        #Display image changed
    except:
        if (filename != ""):
            messagebox.showerror("Incompatible File Error", "The file you have chosen is incompatible. Please select an image file and try again. If this error cannot be resolved, please report it to me at mauricerizat@gmail.com")
    

def removeBkg():
    """
    This functions performs the removal of grid background 
    Called by press of removeBkgButton
    """
    global filename, tolerancePercent, outputFile, photo1 #Global variables to use
    
    try:      
        #Check for no file chosen
        if (filename == "none" or filename == ""):
            messagebox.showerror("Error! File Not Selected.", "Please select a file and try again")
            return #Show error message and cancel process if no file chosen   
        
        removeBkgButton.config(text="PROCESSING...")
        window.update()        
        
        #Processing output file path. Output will be in same directory with user-provided name
        outputFileName = outputFileNameEntry.get();
        outputDirectory = filename[0:filename.rfind("/")+1]
        outputFile = outputDirectory + outputFileName + ".png"    
        
        #Open slected image
        initialImage = Image.open(filename)
        image1 = Image.new("RGBA", initialImage.size)
        image1.paste(initialImage)   
        width, height = image1.size
        image2 = Image.new('RGBA', (width + 1, height)) # Create new image with same size as input image
                
        #print(list(image1.getdata()))      
              
        pixels1 = image1.load() #Get pixel map
        pixels2 = image2.load()#Get pixel map
        
        #Calculate tolerance accorgding to user input
        tolerancePercent = 100-toleranceSlider.get()
        tolerance = tolerancePercent*1.0/100
    
        #Calculate uppper and lowe bounds based on tolerance
        upperbound1 = (int)((1.0+tolerance)*255)
        lowerbound1 = (int)((1.0-tolerance)*255)
        upperbound2 = (int)((1.0+tolerance)*204)
        lowerbound2 = (int)((1.0-tolerance)*204)    
        #By default this program works on removing grey and white grids
                              
        #Actual processing
        for i in range(image1.size[0]): #Column
            for j in range(image1.size[1]): #Row
                r, g, b, a = image1.getpixel((i, j)) #Get individual red, green, blue and intensity values
                #print("Index ", i, ", ", j, ": ", image1.getpixel((i, j)))
                
                if (((r>lowerbound1 and r<upperbound1) and
                     (g>lowerbound1 and g<upperbound1) and
                     (b>lowerbound1 and b<upperbound1)) 
                    or
                    ((r>lowerbound2 and r<upperbound2) and
                     (g>lowerbound2 and g<upperbound2) and
                     (b>lowerbound2 and b<upperbound2))):
                    pixels2[i, j] = (255, 255, 255, 0); #If pixel is part of grid, make it transparent
                else:
                    pixels2[i, j] = pixels1[i, j] #Otherwise just copy the original pixel
                
        image2.save(outputFile) #Save new image to given output file in same directory
        
        messagebox.showinfo("Success!", "Image successfully saved") #Display success message
        
        removeBkgButton.config(text="Remove Grid Background")
        
    except Exception as e: 
        messagebox.showerror("Critical Error! 8990", "A critical error has occured. If this error cannot be resolved, please report it to me at mauricerizat@gmail.com")
    
#Main    
window = Tk() #Creating Root Window
window.title("PNG Grid Background Remover") #Title of window
window.configure(background="gray") #Window background
window.geometry("1000x750") #Window dimensions

#Header
appHeader = Label(window, text="Welcome to PNG Grid Background Remover", bg="white", fg="black", font="none 26 bold italic")
#grid(row=0, column=0, sticky=W)

#Image to display

imageFirst = Image.open(resource_path("theme.jpg")) #Initial starter image. This cannot be processed
imageFirst = imageFirst.resize((300, 350), Image.ANTIALIAS) #Resize image as it is only for reference purpose
photo1 = ImageTk.PhotoImage(imageFirst) #Put image in photo
photoLabel = Label(window, image=photo1, bg="white") #Store photo in label


#Input Elements
inputStuff = Frame(bg="white") #Frame that stores all input fields
selectFileButton = Button(inputStuff, text="Select File", font="none 15", width=15, command=fileSelect) #Button to select image file
toleranceText = Label(inputStuff, text="Select Tolerance Percentage: ", fg="black", font="none 15") #Tolerance text
toleranceSlider = Scale(inputStuff, from_ = 0, to = 100, orient = HORIZONTAL, width=15, length=200) #Slider for tolerance
toleranceSlider.set(50) #Default tolerance value is 50%
selectFileButton.grid(row=0, column=0, padx=30) #Insert button in frame inputStuff
toleranceText.grid(row=0, column=1) #Insert text in frame inputStuff
toleranceSlider.grid(row=0, column=2) #Insert slider in frame inputStuff
outputFileNameText = Label(inputStuff, text="Enter Output File Name (without extension): ", fg="black", font="none 15") #Accept output file name
outputFileNameEntry = Entry(inputStuff, width=20, font="none 15") #Text field for output file name
outputFileNameEntry.insert(0, "defaultOutput") #Default output file name is "defaultOutput"
outputFileNameText.grid(row=1, column=0, padx=30, pady=10) #Insert output file name prompt in frams inputStuff
outputFileNameEntry.grid(row=1, column=1, pady=10) ##Insert output file name text field in frame inputStuff

#Remove Background button
removeBkgButton = Button(window, text="Remove Grid Background", font="none 15", width=25, command=removeBkg) #Button to begin background removal

#Pack all relevant elements into Window
appHeader.pack(pady=50) #Header
photoLabel.pack(pady=15) #Contains display photo
inputStuff.pack(pady=15) #Contains all input fields
removeBkgButton.pack(pady=15) #Contains Remove Background button

bugsReport = Label(window, text="To report bugs and errors please reach me at mauricerizat@gmail.com", bg="gray", fg="black", font="none 12 italic")

bugsReport.pack()

window.mainloop() #Loop
