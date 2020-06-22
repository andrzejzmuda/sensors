import urllib2
import requests


savedEvent = list(open('eventLog2.txt', 'r'))[0]

url = 'http://url:port/write?db=dbname'
logs = urllib2.urlopen("http://url_to_scrape")
lastEvent = str((logs.read())[770:820].rpartition('</a>')[0]).replace('\n\r\n ', '')

handle = open('eventLog2.txt', 'w')
handle.write(lastEvent)
handle.close()
requests.post(url, auth=('login', 'pass'), data='ups_edv2,edv=2 latestEvent="{0}"'.format(lastEvent))
print(lastEvent)
