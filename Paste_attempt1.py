# import image module from pillow 
from PIL import Image 
  
# open the image 
Image1 = Image.open('rawr.jpeg') 
  
# make a copy the image so that the  
# original image does not get affected 
Image1copy = Image1.copy() 
Image2 = Image.open('earth.png') 
Image2copy = Image2.copy() 
  
# paste image giving dimensions 
Image1copy.paste(Image2copy, (0, 0)) 
  
# save the image  
Image1copy.save('D:\pasted2.png') 