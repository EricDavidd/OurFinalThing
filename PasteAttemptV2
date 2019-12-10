
# import image module from pillow 
from PIL import Image 
import os.path
import PIL
  
# open the image 
directory = os.path.dirname(os.path.abspath(__file__))
logo_file = os.path.join(directory, 'ISTE_logo.jpg')
logo_pic = Image.open(logo_file) 
logo_image = logo_pic.resize((270, 114))
  
# make a copy the image so that the  
# original image does not get affected 
logo_imagecopy = logo_image.copy() 
background_file = os.path.join(directory, 'class.jpg')
background_image = Image.open(background_file) 
background_imagecopy = background_image.copy() 
  
# paste image giving dimensions 
position = ((background_image.width - logo_image.width), (background_image.height - logo_image.height))
background_imagecopy.paste(logo_image, position) 
background_image.paste(logo_image, position)

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

# save the image
file_list, image_list = get_images(directory)
new_directory = os.path.join(directory, 'modified')
new_image_filename = os.path.join(new_directory, 'ahh' + '.png')  
background_image.save(new_image_filename)
