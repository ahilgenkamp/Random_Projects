from PIL import Image
import numpy as np
import glob
import os
import math
import time
from matplotlib import pyplot as plt


imgList = glob.glob(os.getcwd()+"\\ToothbrushTimelapse\\*.jpg") + \
            glob.glob(os.getcwd()+"\\KitchenTimelapse\\*.jpg") + \
            glob.glob(os.getcwd()+"\\WorkTimelapse\\*.jpg")


def get_concat_h(im1, im2, cols=8):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def timelapseToImage(imgList):
	totalImgs = len(imgList)
	start = time.time()
	counter = 0
	for im in range(0,len(imgList[:math.floor(math.sqrt(len(imgList)))**2])):
	    totalLen = len(imgList[:math.floor(math.sqrt(len(imgList)))**2]) 
	    
	    if im % math.floor(math.sqrt(totalImgs)) == 0 and im == 0:
	        im_row = Image.open(imgList[im])
	    elif im % math.floor(math.sqrt(totalImgs)) == 0 and im == math.floor(math.sqrt(len(imgList))):
	        im_row = im_row.resize((im_row.width // math.floor(math.sqrt(len(imgList))), 
	                                im_row.height // math.floor(math.sqrt(len(imgList)))))
	        im_new = im_row
	        im_row = Image.open(imgList[im])
	    elif im % math.floor(math.sqrt(totalImgs)) == 0:
	        im_row = im_row.resize((im_row.width // math.floor(math.sqrt(len(imgList))), 
	                                im_row.height // math.floor(math.sqrt(len(imgList)))))
	        im_new = get_concat_v(im_new, im_row)
	        im_row = Image.open(imgList[im])
	    else:
	        im_add = Image.open(imgList[im])
	        im_row = get_concat_h(im_row, im_add)
	    counter += 1
	    print('\rIteration '+str(counter)+' of '+str(totalLen)+' completed', end='', flush=True)

	print('\nCompleted in '+str(round(time.time()-start,3))+' sec')
	print(im_new.size)
	return im_new

