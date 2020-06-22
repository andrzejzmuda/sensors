import json, urllib2, requests, datetime
url = 'http://url:port/write?db=dbname'
link = urllib2.urlopen('http://url/json')
d = json.loads(str(link.read()))
index = ('outside_temp', 'outside_humid',
         'inside_up_temp', 'inside_up_humid',
         'inside_bottom_temp', 'inside_bottom_humid')
for i in d['Sensors']:
    temp = "esp000temp_" + str(i['TaskName']) +"=" + "%.2f" % float(str(i['TaskValues'][0]['Value']))
    humid = "esp000humid_" + str(i['TaskName']) +"=" + "%.2f" % float(str(i['TaskValues'][1]['Value']))
    requests.post(url, auth=('login', 'pass'), data="dbname,sensor=esp000 {0},{1}".format(temp, humid))
    file_path = '/path/to/txt_file/esp000_report.txt'
    handle = open(file_path, 'w')
    handle.write("last entry: " + str(datetime.datetime.now()))
    handle.close()
