#!/usr/bin/python

import mechanize # for emulating browser

try:
    # Start fake browser 
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)')]
    # Attempt to open url with fake browser
    url = "http://www.example.com"
    try:
        br.open(url)
    # Exit if url fails to open
    except mechanize.URLError:
        print "URL '%s' failed to open, exiting." % url
        raise SystemExit

    # List forms on page
    #for f in br.forms():
        #print f
    
    # Fill out form and attempt login
    # Username and password are in separate forms 
    br.select_form(nr=0)
    br.form['user'] = 'USERNAME'
    br.select_form(nr=1)
    br.form['pass'] = 'PASSWORD' 
    br.submit()

    # Read the html
    html = br.response().read()
    if "Error" in html:
        print "Login failed"
    else:
        # replace with some success case, e.g.: 
        # elif "Welcome" in html
        print "Login may have worked"

except KeyboardInterrupt:
    print "\n"
