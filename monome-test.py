#! /usr/bin/env python

import time, random
from monome import Monome, MonomeBrowser

# lookup for monome (can skip this if you know the host/port)
serial = 'a40h-458'
browser = MonomeBrowser()
browser.start()
print "looking for %s" % serial
while not browser.devices.has_key(serial):
    time.sleep(0)
print "found!"
host, port = browser.devices[serial]

# connect to the monome
m = Monome('localhost', port) # don't use resolved host, 'cause it doesn't work
m.start() # begin processing callbacks

def mycallback(addr, data):
    print "received", addr, data

m.app_callback = mycallback

m.led_all(0)
while True:
    for i in range(8):
        m.led_row(0, i, random.randint(0,255))
        time.sleep(0.2)
