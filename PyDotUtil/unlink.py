import lib, os

home = lib.getHomeFolder()

def run(path):
  if lib.checkFileList(path):
    for file in os.listdir(path):
      link = os.path.join(home, file)
      
      # Someday, this should return a count/list of files that were removed
      if os.path.islink(os.path.join(home, file)):
        os.unlink(link)