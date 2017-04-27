#!/usr/bin/env python
#-*- coding: utf-8 -*-

from selenium import webdriver
import time, os, sys
import checkCrawlerd as c

def connect(ip, port):
	
	if c.ip_in_crawlerd(ip) == False:
		
		c.write_to_crawlerd(ip+"\n")

		profile = webdriver.FirefoxProfile()
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", ip)
		profile.set_preference("network.proxy.http_port", port)
		profile.update_preferences()
		driver = webdriver.Firefox(firefox_profile=profile) 
     
		try:
			driver.get('http://babblecase.com/bXp')
		except:
			print "error"
			return "error"
			driver.quit()
			sys.exit()

		time.sleep(10)
		driver.quit()
	else:
		return False
		
	#connect("172.245.59.203", 7808) 
