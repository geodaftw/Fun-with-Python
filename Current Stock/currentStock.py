#! python.3
# Check current stock
# Written by: Eric Guillen

# TODO: Type "Help" and get a list of common ones I like

import webbrowser, sys
import requests
import re

print("[+] Check the Stock")
print("[+] You normally like CERN, CTL")
print("[+] What Stock symbol are you wanting?")
symbol = input()


#webbrowser.open('https://money.cnn.com/quote/quote.html?symb=' + symbol)

# Use requests to access the page. If it fails, print exception
res = requests.get('https://money.cnn.com/quote/quote.html?symb=' + symbol.upper())
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# RegEx to extract information from page
title = re.search(r'\<title\>(.*?)\<\/title\>', res.text).group(1)
#current = re.search(r'ToHundredth\" streamFeed\=\"BatsUS\"\>(.*?)\<\/span\>\<div', res.text).group(1)
#posChange = re.search(r'streamFeed\=\"BatsUS\"\>\<span class\=\"posData\"\>(.*?)\<\/span\>\<\/span\>\<span', res.text).group(1)
#negChange = re.search(r'streamFeed\=\"BatsUS\"\>\<span class\=\"negData\"\>(.*?)\<\/span\>\<\/span\>\<span', res.text).group(1)

print("[*] " + title + " [*]")
#print("[+] Current is: " + current)
#print("[+] Currently it is: " + str(posChange))
