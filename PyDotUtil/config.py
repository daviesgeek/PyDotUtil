import os, ConfigParser

config = ConfigParser.RawConfigParser()

def run(args):
  if(os.path.isdir(args['dir'])):
    config.add_section('Main')
    config.set('Main', 'repo', args['dir'])

    with open('config.cfg', 'wb') as configfile:
        config.write(configfile)
  else:
    print "Directory '"+args['dir']+"' doesn't exist"