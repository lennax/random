#!/usr/bin/python

import urllib2

url1 = "https://my.ipfw.edu"
url2 = "http://fjjdjjdjdj.de"

try: 
    urllib2.urlopen(url1)
    success1 = 1
except urllib2.URLError:
    print "URL '%s' failed to open" % url1
if success1:
    print "URL '%s' opened successfully" % url1



