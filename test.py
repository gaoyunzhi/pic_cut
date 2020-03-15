#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pic_cut

def test():
	assert len(list(pic_cut.cut('tmp/no_cut.jpg')))	== 0
	list(pic_cut.cut('tmp/no_cut_2.jpg'))
	list(pic_cut.cut('tmp/cut_1.jpg'))
	list(pic_cut.cut('tmp/cut_2.jpg'))
	
if __name__=='__main__':
	test()