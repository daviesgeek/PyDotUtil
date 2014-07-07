import glob, os, argparse

parser = argparse.ArgumentParser(description='Simple dotfiles symlinking')
parser.add_argument('-f', '--force', help='Force overwriting of existing files', required=False, action='store_true')
parser.add_argument('-r', '--remove', help='Unsymlink the files', required=False, action='store_true')
args = vars(parser.parse_args())

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'home')
home = os.path.expanduser("~")
filelist = os.listdir(path)

if(args['remove']):
  for file in os.listdir(path):
    link = os.path.join(home, file)
    
    # Someday, this should return a count/list of files that were removed
    if os.path.islink(os.path.join(home, file)):
      os.unlink(link)
else:
  for file in os.listdir(path):
    dest = os.path.join(home, file)
    src = os.path.join(path, file)

    # Someday, this should return a count/list of files that were linked
    if not os.path.islink(os.path.join(home, file)):
      os.symlink(src, dest)