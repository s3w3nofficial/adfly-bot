#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib

def connect(ip, port):

	proxy = {"http" : "http://" + ip + ":" + port}
	proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
	print proxy
	 
#connect("107.0.69.165", "3128") 
