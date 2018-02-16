import urllib
import requests
import time
import os
import sys
sys.stdout.flush()
url = 'http://www.way2sms.com'

response = requests.head(url, allow_redirects=True)
new_url = response.url
ses = requests.session()
ses.headers.update({'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
                     'Upgrade-Insecure-Requests': '1',
                     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                     'DNT': '1', 'Accept-Encoding': 'gzip, deflate',
                     'Accept-Language': 'en-US,en;q=0.8'})
usr = str("YOUR_USER_NAME")
pas = "PASSWORD"
if ses.post(new_url + 'Login1.action', 'username=' + str(usr) + '&password=' + str(pas)).ok:
    print "Login successfully"
    token = ses.cookies['JSESSIONID']
    token = token[4:]
else:
    print "Login failed"

mobile = str("RECEIVERS MOBILE NO")
string = str("YOUR_MESSAGE")

mobile = list(str(mobile).split(','))

for mobile_no in mobile:
    lofstr = list(str(string).split(','))
    for string in lofstr:
        msglen = len(string)
        qstring = urllib.quote(string)
        page = ses.post(new_url+'smstoss.action', 'ssaction=ss&Token='+str(token)+'&mobile='+str(mobile_no)+'&message='+qstring+'&msgLen='+str(140-msglen)).text
        print 'Sending SMS to', mobile_no,
        for dot in range(3):
            print '.',
            time.sleep(1)
#logout
ses.get(new_url+'main.action')
