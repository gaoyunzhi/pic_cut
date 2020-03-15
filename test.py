#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pic_cut
import os
import sys

def test():
	additional_setting = '--paper-size b6 --pdf-page-margin-left 15 ' + \
		'--pdf-page-margin-right 15 --pdf-page-margin-top 15 ' + \
		'--pdf-page-margin-bottom 15'
	pdf_name = pic_cut.gen(news_source='bbc', 
		filename_suffix='_大字版', additional_setting=additional_setting)
	os.system('open %s -g' % pdf_name)
	
	
if __name__=='__main__':
	test()