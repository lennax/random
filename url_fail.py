#!/usr/bin/python

import urllib2

url1 = "https://my.ipfw.edu"
url2 = "http://fjjdjjdjdj.de"


def test_url(url1):
    try:
        urllib2.urlopen(url1)
    except urllib2.URLError:
        print "URL '%s' failed to open" % url1
    else:
        print "URL '%s' opened successfully" % url1


test_url(url1)
test_url(url2)
