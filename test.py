#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pic_cut
import web_2_album

def test():
	result = web_2_album.get('https://www.douban.com/people/2627485/status/3185647338/')
	print(pic_cut.getCutImages(result.imgs, limit=100))
	
if __name__=='__main__':
	test()