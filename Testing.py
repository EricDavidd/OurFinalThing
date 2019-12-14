'''
HOW TO USE PROGRAM: Put this canopy file in the folder of where all of the pictures are located at with the ISTE logo being named 'logo.jpg', run the program,
and then you can use the brand_image(wide, color) command in the IJupiter place to put the ISTE logo. It will then proceed to make
a folder called "modified" and the modified images will be in there. Then, it places colored corners on them, put in the command
with the color for the brand_image() function using RGB format, like this (0, 255, 0), to get green or other colors. The wide is inputted
from the user of how many pixels big they want the corners. It will then output these modified images in the modified folder.
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
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, color)
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result

            
def brand_image(wide, color):
        directory = os.path.dirname(os.path.abspath(__file__)) # Defines the program's directory to use the working directory.
        new_directory = os.path.join(directory, 'modified') # Assiging the variable new_directory to a new folder called "modified" in the working directory.
        try:
            os.mkdir(new_directory) # Try making a new directory for "modified"
        except OSError: 
            pass
        
        image_list, file_list = get_images(directory)  
        """ Uses for loop to get out every image from the folder that it is in and then proeeds to use the put_logo function
        to then produce a modified image that is then saved as a png with the same name in a different folder called "modified."
        """
        for n in range(len(image_list)):
            filename, filetype = file_list[n].split('.') # With all of the images, it can see the images split with the '.'
        
            background_image = put_logo(image_list[n]) # Using put_logo function
            new_directory = os.path.join(directory, 'modified') # Assigning where new_directory is
            new_image_filename = os.path.join(new_directory, filename + '.png') # Saves the image as .png into the new folder from new_directory.
            background_image.save(new_image_filename) # Saves the image into the modifeied folder with the same name, as a png.
        
        """ Uses for loop to get out every image from the modified folder that already has the logos pasted, and then proeeds to use the put_corners function
        to then produce a modified image that is then saved as a png with the same name in a different folder called "modified."
        """
        newimage_list, newfile_list = get_images(new_directory) # Changes the image list to focus on the photos in the new_directory.
        
        for n in range(len(newimage_list)):
            filename, filetype = newfile_list[n].split('.')
            
            new_image = put_corners(newimage_list[n], wide, color) # Uses put_corners function and uses the user input for wide and color to input into the function.
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename)
            
            