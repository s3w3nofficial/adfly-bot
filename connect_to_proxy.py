#!/usr/bin/env python
#-*- coding: utf-8 -*-

from selenium import webdriver
import time, os

def connect(ip, port):

	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http", ip)
	profile.set_preference("network.proxy.http_port", port)
	profile.update_preferences()
	driver = webdriver.Firefox(firefox_profile=profile) 

	driver.get('http://whatismyip.cz')
	time.sleep(5)
	driver.close()	 
