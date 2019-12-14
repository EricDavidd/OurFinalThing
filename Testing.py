'''
HOW TO USE PROGRAM: Put this canopy file in the folder of where all of the pictures are located at with the ISTE logo being named 'logo.jpg', run the program,
and then you can use the add_logo() command in the IJupiter place to put the ISTE logo. It will then proceed to make
a folder called "modified" and the modified images will be in there. To place a colored corners on them, put in the command
corner_all_images(color, wide) with the color using RGB format, like this (0, 255, 0), to get green or other colors.
It will then output these modified images in the modified folder.
'''


# import image module from pillow 
from PIL import Image 
import os.path
import os
import PIL

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        


directory = os.path.dirname(os.path.abspath(__file__)) #specify which directory to find the photos.

logo_file = os.path.join(directory, 'logo.jpg') # Assign 'logo_file' as the directory of where the logo image is.
logo_pic = Image.open(logo_file) # Open the logo file.
logo_image = logo_pic.resize((270, 114)) # Resize the logo image to be smaller.
logo_imagecopy = logo_image.copy() # Copy the image.


def put_logo(background_image): 
        # paste image giving dimensions that allow it to put the logo in the bottom right
        position = ((background_image.width - logo_image.width), (background_image.height - logo_image.height))
        background_image.paste(logo_image, position)
        image_list, file_list = get_images(directory) # Making image_list, and file_list as the variable which uses the defined function of get_images. Allowing the program to get all of the images in the folder.
        background_image.save # Save the new background_image, after the logo has been pasted onto it.
        return background_image # Returns the saved image back to the defined function of add_logo to be saved.
        
def corner_all_images(color, wide, directory=None):
    directory = os.path.dirname(os.path.abspath(__file__))
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
        
    image_list, file_list = get_images(directory)  
    
    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
        
        new_image = put_corners(image_list[n], wide, color)
        
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
                    
def put_corners(original_image, pixels, color):
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(pixels) # radius in pixels
    
    ###
    #create a mask
    ###
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=color)
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=color)
    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=color) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=color) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=color) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=color) #bottom right
                        
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (255,255,0,255))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result

            
def brand_image():
        directory = os.path.dirname(os.path.abspath(__file__)) # Defines the program's directory to use the working directory.
        new_directory = os.path.join(directory, 'modified') # Assiging the variable new_directory to a new folder called "modified" in the working directory.
        try:
            os.mkdir(new_directory) # Try making a new directory for "modified"
        except OSError: 
            pass
        
        image_list, file_list = get_images(directory)  
    
        for n in range(len(image_list)):
            filename, filetype = file_list[n].split('.')
        
            background_image = put_logo(image_list[n])
            new_directory = os.path.join(directory, 'modified')
            new_image_filename = os.path.join(directory, filename + '.png')
            background_image.save(new_image_filename)
            