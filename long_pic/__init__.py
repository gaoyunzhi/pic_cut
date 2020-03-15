#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'pic_cut'

import Image
import math
import os

def goodSize(w, h):
	return h < 2 * w

def computeSize(h, p):
	return math.ceil(h / (p - 0.05 * (p - 1)))

def cut(path):
    img = Image.open(path)

    w, h = img.size

    for piece in range(1, 10):
    	nh = computeSize(h, piece)
    	if goodSize(w, nh):
    		break
    if piece == 1 or not goodSize(w, nh):
    	return

    upper = 0
    lower = h - (piece - 1) * nh

    for p in range(piece):
        working_slice = img.crop((0, upper, w, lower))
        main_path, _ = os.path.splitext(path)
        working_slice.save('%s_%d.png' % (main_path, p))
        upper += nh
        lower += nh

