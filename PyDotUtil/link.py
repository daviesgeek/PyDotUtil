import lib, os

home = lib.getHomeFolder()

def run(path):
  if lib.checkFileList(path):
    for file in os.listdir(path):
      dest = os.path.join(home, file)
      src = os.path.join(path, file)

      # Someday, this should return a count/list of files that were linked
      if not os.path.islink(os.path.join(home, file)):
        os.symlink(src, dest)