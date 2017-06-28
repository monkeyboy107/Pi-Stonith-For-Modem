import os
import yaml

def loadConfig():
  '''
  Loads config from known YAML files
  :return: dict of config from YAML
  '''
  config_paths = [
    'pistonithformodem',
    'pistonithformodem.yaml',
    os.path.expanduser('~/pistonithformodem'),
    os.path.expanduser('~/.pistonithformodem'),
    os.path.expanduser('~/pistonithformodem.yaml'),
    os.path.expanduser('~/.pistonithformodem.yaml'),
    os.path.expanduser('~/.config/pistonithformodem/config.yaml'),
    '/etc/pistonithformodem/config.yaml'
  ]
  config_file = None
  for path in config_paths:
    if os.path.isfile(path):
      config_file = path
      break
  try:
    assert config_file != None
  except:
    raise Exception('Cannot find config file in {}'.format(str(config_paths)))
  try:
    with open(config_file,'r') as f:
      config = yaml.load(f.read())
  except:
    raise Exception('Cannot load YAML from {}'.format(config_file))
  if config == None:
    config = {}
  return(config)

