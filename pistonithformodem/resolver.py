import os

class Resolver(object):
  '''
  Resolves a DNS record
  '''

  def __init__(self,name,dns_server='192.168.1.1'):
    self.name       = name       ## Add name param to object
    self.dns_server = dns_server ## DNS server to query

  def run(self):
    '''
    Perform the resolution
    :return:
    '''
    cmd = "dig @{} {}".format(self.dns_server,self.name)
    if os.system(cmd) == 0: ## Runs the command and if the result is 0, then it was good
      return(True)
    else:
      return(False)

