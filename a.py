import os
def run(**args):
  print "[*] In a module."
  files = os.listdir(".")
  return str(files)
