import requests
from requests.compat import urljoin, quote_plus

class Modem(object):
  def __init__(self,password,username='admin',prefix='http://192.168.1.1'):
    self.username = username
    self.password = password
    self.prefix = prefix
    self.loginURL = self.cobbleURL('login.cgi')

  def cobbleURL(self,path):
    return(urljoin(self.prefix, quote_plus(path)))

  def reboot(self):
    session = requests.session()
    session.post(self.loginURL, data={
      "admin_username": self.username,
      "admin_password": self.password
    })
    session.post(self.cobbleURL('utilities_reboot.cgi'))
    session.post(self.cobbleURL('apply_real.cgi'))
    session.close()

  def uptime(self):
    url = self.cobbleURL('modemstatus_internetstatus.html')
    session = requests.session()
    session.post(self.loginURL, data={
      "admin_username": self.username,
      "admin_password": self.password
    })
    html = session.get(url).text
    for line in html.split('\n'):
      if 'modemUpTime' in line:
        uptime = line.split('>')[3].split('<')[0]
    session.close()
    minutes = int(uptime.split('M')[0])
    seconds = int(uptime.split(':')[-1].split('S')[0])
    return((minutes*60)+seconds)


modem = Modem('')
#modem.reboot()
import time
while True:
  print modem.uptime()
  time.sleep(1)

