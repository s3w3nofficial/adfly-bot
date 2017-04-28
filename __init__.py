#!/usr/bin/env python
#-*- coding: utf-8 -*-

from threading import Thread
import crawler as cw
import connect_to_proxy as ctp
import time

def main():
	t1 = Thread(target=run)
	t2 = Thread(target=run)
	t1.start()
	t2.start()
	print "Complete"

def run():
	page = cw.get_ip_port()
	ip = ""
	port = "" 
	
	#print page[0][0], page[1][0]
	for ip in page[0]:
		for port in page[1]:
			print ip, port
			if init(ip, port) == False:
				time.sleep(12)
	
def init(ip, port):
	ctp.connect(ip, int(port))
	return True

if __name__ == "__main__":
	main()
