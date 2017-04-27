#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import html
import requests

def get_ip_port():
	page = requests.get('https://free-proxy-list.net/')
	page = html.fromstring(page.content)

	ips = page.xpath('//div/table/tbody/tr/td[position()=1]/text()')
	ports = page.xpath('//div/table/tbody/tr/td[position()=2]/text()') 
	ip_list = []
	port_list = []

	for ip in ips:
		ip_list.append(ip)
	for port in ports:
		port_list.append(port)

	#print ip_list
	#print port_list	
	return ip_list, port_list
