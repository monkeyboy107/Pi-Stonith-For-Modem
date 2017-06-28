#!/usr/bin/python
from utils import *
from pinger import *
from resolver import *

def shell():
  '''
  This is the function to handle the command line interaction
  :return:
  '''

  ## This loads the config from the method in the pistonithformodem/utils.py called `loadConfig`
  config = loadConfig()
  if 'debug' in config.keys() and config['debug']:
    print(config)

  ## This creates a list of instances of Pinger objects based on the key `ping` in the config
  ping_targets = []
  if 'ping' in config.keys():
    try:
      assert type(config['ping']) == type([])
    except:
      raise Exception('the key "ping" must be a list')
    for target in config["ping"]:
      ping_targets.append(Pinger(host=target))

  ## This creates a list of instances of Resolver objects based on the key `resolve` in the config
  resolve_targets = []
  if 'resolve' in config.keys():
    try:
      assert type(config['resolve']) == type([])
    except:
      raise Exception('the key "resolve" must be a list')
    for target in config["resolve"]:
      resolve_targets.append(
        Resolver(
          name=target,
          dns_server=config["dns_server"]
        )
      )


  tests = ping_targets+resolve_targets
  if not all(
      map(
        lambda job: job.run(), tests
      )
  ):
    print("Some tests failed, soft rebooting modem")
    while not all(
        map(
          lambda job: job.run(), tests
        )
    ):
      print("waiting for modem to come back")
