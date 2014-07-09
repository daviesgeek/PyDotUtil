import sys, os

def checkFileList(path):
  try:
    filelist = os.listdir(path)
    return True
  except Exception, e:
    print e
    print "The path `"+path+"` does not exist"
    print "Please change repo path either in the configuration file or by using the config option"
    sys.exit()

def getHomeFolder():
  return os.path.expanduser("~")