from ftplib import FTP
import requests
import datetime


ftp = FTP('address')
ftp.login('login', 'pass')
ftp.cwd('logs')
ftp.retrbinary('RETR event.txt', open('event_edv3.txt', 'wb').write)
ftp.quit()

url = 'http://url:port/write?db=dbname'

eventsList = open("event_edv3.txt", "r")
event = list(eventsList)
eventsList.close()
for n in event[8:]:
    if 'user' not in n:
        latestEvent = n.split('\r\n')[0]
        savedEvent = list(open('eventLog3.txt', 'r'))[0].replace('\t', ' ').split('\r\n')[0]
        if latestEvent != savedEvent:
            handle = open('eventLog3.txt', 'w')
            handle.write(latestEvent)
            handle.close()
            requests.post(url, auth=('login', 'pass'), data='ups_edv3,edv=3 latestEvent="{0}"'.
                          format(latestEvent))
        else:
            handle = open('eventLog3.txt', 'w')
            handle.write(str(datetime.datetime.now) + "no news is good news")
            handle.close()
        break
