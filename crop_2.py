from PIL import Image

def black_and_white(input_image_path,output_image_path):
   size = 200,200
   im= Image.open(input_image_path)
   im_resized = im.resize(size, Image.ANTIALIAS)
   im_resized = im_resized.convert('L')
   im_resized.save(output_image_path)
  #1920x1080_wallpaper_242.jpg this is target file
  #this is result file
 
if __name__ == '__main__':  
    black_and_white('1920x1080_wallpaper_242.jpg','resized.jpg')
