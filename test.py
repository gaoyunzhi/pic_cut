#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pic_cut
import web_2_album
import weibo_2_album

def test():
	result = weibo_2_album.get('https://m.weibo.cn/detail/4585474025325107#comment')
	print(pic_cut.getCutImages(result.imgs, limit=100))
	
if __name__=='__main__':
	test()