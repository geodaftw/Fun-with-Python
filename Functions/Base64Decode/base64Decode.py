#!/usr/bin/python

import base64

f = open('screenshot1.bmp', 'r').read()
decoded = base64.b64decode(f)
g = open('finalScreenshot.bmp', 'w')
g.write(decoded)
#f.close()
g.close()
