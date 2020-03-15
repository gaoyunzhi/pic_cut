#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'pic_cut'

import Image
import math
import os

def goodSize(w, h):
	return h < 2 * w

def computeSize(h, p):
	return h / (p - 0.05 * (p - 1))

def cut(path):
    img = Image.open(image_path)

    w, h = img.size

    for piece in range(1, 10):
    	nh = computeSize(h, piece)
    	if goodSize(w, nh):
    		break
    if piece == 1 or not goodSize(w, nh):
    	return

    upper = 0

    for p in range(piece):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  
        #set the bounding box! The important bit     
        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(count)+".png"))
        count +=1

