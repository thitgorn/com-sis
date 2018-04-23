import sys
import os
import numpy as np
import cv2

def split_into_rgb_channels(image):
  '''Split the target image into its red, green and blue channels.
  image - a numpy array of shape (rows, columns, 3).
  output - three numpy arrays of shape (rows, columns) and dtype same as
           image, containing the corresponding channels.
  '''
  red = image[:,:,2]
  green = image[:,:,1]
  blue = image[:,:,0]
  return red, green, blue

def main( path ):
  ''' This function searches for a folder images/knowpapa subfolder, and splits
   all images found in that folder into its equivalent rgb channel.
   It saves each image appending the terms 'red', 'green' and
  'blue' to the orginal filename.
  '''
  imagesdir = os.path.abspath(os.path.join(os.curdir, path))
  print ("Searching for images in {} Directory)".format(imagesdir))
  exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg',
    '.jpe', '.jp2', '.tiff', '.tif', '.png']
  total = 0
  for dirname, dirnames, filenames in os.walk(imagesdir):
    for filename in filenames:
      if filename == '.DS_Store':
          continue
      count = 0
      print (filename)
      name, ext = os.path.splitext(filename)
      img = cv2.imread(os.path.join(dirname, filename))
      # print (img)
      red, green, blue = split_into_rgb_channels(img)
      for i in range(len(red)):
          for j in range(len(red[i])):
              if red[i][j] == 0 and green[i][j] == 0 and blue[i][j] == 0:
                  count+=1
                  red[i][j] = 255;
                  green[i][j] = 255;
                  blue[i][j] = 255;
      print ("there are %d black pixel in Image" % count)
      total+=count
      img = np.zeros((len(red), len(red[0]), 3), np.uint8)
      img[:,:,2] = red
      img[:,:,1] = green
      img[:,:,0] = blue
      print ("writing %s file" % name+"-new"+ext)
      cv2.imwrite(os.path.join(dirname,name+"-new"+ext),img)
      print ()
  print ("total black pixel %d" % total)

if __name__ == "__main__":
    main(sys.argv[1])
