#!/usr/bin/env python
#-*- coding: utf-8 -*-

import crawler as cw
import connect_to_proxy as ctp
import time

def main():
	page = cw.get_ip_port()
	
	print page[0][0], page[1][0]
	for ip in page[0]:
		for port in page[1]:
			print ip, port
			ctp.connect(ip, port)
			time.sleep(6)

if __name__ == "__main__":
	main()
