__author__ = 'pabloholanda'
import urllib2
from time import sleep

while True:
    try:
        code = urllib2.urlopen("http://127.0.0.1:8000", timeout=1).getcode()
        print code
    except urllib2.URLError as e:
        if str(e.reason) == 'timed out':
            print "Timed out"
        elif str(e.reason) == '[Errno 61] Connection refused':
            print "Refused"

    sleep(10)
