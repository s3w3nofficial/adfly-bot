#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re

proxy = {'http' : 'http://167.114.0.241:3128'}
proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
proxy = re.findall(r'"([^"]*)"', proxy)
print proxy[1]
