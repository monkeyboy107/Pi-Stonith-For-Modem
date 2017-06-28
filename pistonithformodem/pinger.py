import os

class Pinger(object):
  '''
  Handles monitoring by pinging a given host
  '''

  def __init__(self,host,count=1):
    '''
    Constructor
    :param host: hostname or ip of monitored host
    '''
    self.host = host   ## Add host param to object
    self.count = count ## Number of pings to try before failing

  def run(self):
    '''
    Performs a ping
    :return: If the ping was successful, returns true, else false
    '''
    cmd = "ping -c {} {}".format(str(self.count),self.host) ## Literal string of the ping command to exec
    if os.system(cmd) == 0: ## Runs the command and if the result is 0, then the ping was good
      return(True)
    else:
      return(False)

