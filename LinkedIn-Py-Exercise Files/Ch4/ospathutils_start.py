#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
#from signal import pause
import time


def main():
  # Print the name of the OS
  # print(os.name)
  
  # Check for item existence and type
  # print("item exists : "+str(path.exists("textfile.txt")))
  # print("File exists : "+str(path.isfile("textfile.txt")))
  # print("Directory exists : "+str(path.isdir("textfile.txt")))  
  # Work with file paths
  # print("Item path : "+str(path.realpath("textfile.txt")))
  # print("Path and name : "+str(path.split(path.realpath("textfile.txt"))))

  
  # # Get the modification time
  # t=time.ctime(path.getmtime("textfile.txt"))
  # print(t)
  # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

  
  # Calculate how long ago the item was modified
  td=datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("It has been "+ str(td) + " since the file was modified")
  print("Or, "+str(td.total_seconds())+" seconds")
  

if __name__ == "__main__":
  main()
