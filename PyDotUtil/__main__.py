import glob, os, argparse, ConfigParser, sys
import config, link, unlink, lib

configFile = ConfigParser.RawConfigParser()
configFile.read('config.cfg')

try:
  repo = configFile.get('Main', 'repo')
  path = os.path.realpath(repo)
except Exception, e:
  path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../castle')

parser = argparse.ArgumentParser(description="description")
subparsers = parser.add_subparsers(help='modes', dest='mode')

configParser = subparsers.add_parser('config', help='Configuration of PyDotUtil')
configParser.add_argument('-d', '--dir', help='config: The directory that PyDotUtil will read from', action='store', required=False)

linkParser = subparsers.add_parser('link', help='Links all the files/folders')
unlinkParser = subparsers.add_parser('unlink', help='Unlinks all the files/folders')
args = vars(parser.parse_args())

if args['mode'] == 'link':
  link.run(path)
elif args['mode'] == 'unlink':
  unlink.run(path)
elif args['mode'] == 'config':
  config.run(args)