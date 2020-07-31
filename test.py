#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pic_cut

def test():
	print(pic_cut.getCutImages(['https://api.telegram.org/file/bot1079222610:AAFeqXw45QT1Ixhclt12ehXtqh8EXRGChK8/documents/file_6475.jpg'],
		limit=100))
	
if __name__=='__main__':
	test()