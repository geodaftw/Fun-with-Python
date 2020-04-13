#! python3.
# Check what the current Temperature is by zip code
# Written by: Eric Guillen

# TODO: Based off the temperature and if there's sun/couds, suggest clothes

import webbrowser, sys
import requests 
import re # import regexp
import bs4 # import beautifulsoup

dSymbol = u"\u00b0"
if len(sys.argv) > 1:
    # Get zipcode from command line
    zipcode = ' '.join(sys.argv[1:])
else:
    # Exit but provide what should be done
    print('[-] Need to provide a zipcode such as:')
    print('python weatherZipCode.py 66213')
    sys.exit()

# Open Browser and go to the page
#webbrowser.open('https://weather.com/weather/today/l/' + zipcode)

# Use requests to access the page. If it fails, print exception
res = requests.get('https://weather.com/weather/today/l/' + zipcode)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# RegEx to find what City this is
city = re.search(r'title data\-react\-helmet\>(.*?) Weather Forecast', res.text).group(1)
# RegEx to find the current Temperature
temp = re.search(r'today\_nowcard\-temp\"\>\<span class\=\"\"\>(.*?)\<sup\>', res.text).group(1)
# RegEx to find what it feels like
feelsLike = re.search(r'deg\-feels\" className\=\"deg\-feels\"\>(.*?)\<sup\>', res.text).group(1)
# RegEx to find out the Sky: Sunny/Cloud/Etc
sky = re.search(r'div class\=\"today\_nowcard\-phrase\"\>(.*?)\<\/div\>', res.text).group(1)
# RegEx to find what the Wind is
wind = re.search(r'Wind\<\/th\>\<td\>\<span class\=\"\"\>(.*?)\<\/span\>', res.text).group(1)
# RegEx to find out the Humidity
humidity = re.search('Humidity\<\/th\>\<td\>\<span class\=\"\"\>\<span\>(.*?)\<span', res.text).group(1)
# RegEx to find out what the Dew is


print('[+] Weather Report for ' + city)
print('[+] Currently ' + sky + ' at ' + temp + dSymbol)
print('[+] Feels like ' + feelsLike + dSymbol + ' with a ' + wind + 'wind')
    
