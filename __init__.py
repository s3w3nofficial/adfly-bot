#!/usr/bin/env python
#-*- coding: utf-8 -*-

import crawler as cw
import connect_to_proxy as ctp

def main():
	page = cw.get_ip_port()
	
	print page[0][0], page[1][0]
	ctp.connect(page[0][0], page[1][0])

if __name__ == "__main__":
	main()
