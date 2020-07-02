#!/usr/bin/python

import requests # pip install requests
import urllib.request # Needed for the json request at the end
from selenium import webdriver # For selenium
import json # to properly submit json requests
import os # To perform bash commands
import subprocess # To perform bash commands
import pickle # I forget why I have this..
import time # For Sleep
from selenium.webdriver.common.keys import Keys # To use Key commands within Selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # Needed in order to get Browser logs


#################################
## Automate Objective 11 for Holiday Hack Challenge 2019 - KringleCon 2 - Turtle Doves
## Written by Eric Guillen
#################################

## TODO: Permanently set chromedriver to path
## export PATH=$PATH:/Users/canonzalman/Downloads
## create functions and utilize full python and not bash

# Createing an instance webdrivetr
# Will have to remove firefox and switch to chrome
# These allow me to access the console log (get_log('browser')

'''
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
browser = webdriver.Chrome(desired_capabilities=d)
browser.get('https://crate.elfu.org')
browserConsole=browser.get_log('browser')
'''

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

f = open ('variable.txt', 'w')
f.write(html_source)
f.close()

