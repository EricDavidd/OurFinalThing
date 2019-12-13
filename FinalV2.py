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
        


directory = os.path.dirname(os.path.abspath(__file__))

logo_file = os.path.join(directory, 'logo.jpg')
logo_pic = Image.open(logo_file) 
logo_image = logo_pic.resize((270, 114))
logo_imagecopy = logo_image.copy()


def put_logo(background_image): 
        # paste image giving dimensions that allow it to put the logo in the bottom right
        position = ((background_image.width - logo_image.width), (background_image.height - logo_image.height))
        background_image.paste(logo_image, position)
        image_list, file_list = get_images(directory)
        background_image.save
        return background_image

            
def add_logo():
        directory = os.path.dirname(os.path.abspath(__file__))
        new_directory = os.path.join(directory, 'modified')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass
        
        image_list, file_list = get_images(directory)  
    
        for n in range(len(image_list)):
            filename, filetype = file_list[n].split('.')
        
            background_image = put_logo(image_list[n])
            new_directory = os.path.join(directory, 'modified')
            new_image_filename = os.path.join(new_directory, filename + '.png')
            background_image.save(new_image_filename)
