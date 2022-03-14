#
# Read and write files using the built-in Python file methods
#

from stat import filemode
from click import open_file


def main():  
  # Open a file for writing and create it if it doesn't exist
  # f=open("textfile.txt","w+")
  # Open the file for appending text to the end
  # f=open("textfile.txt","a")
  f=open("textfile.txt","r")

  # # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is line "+ str(i)+"\r\n")

  
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode=="r":
    # contents = f.read()
    # print(contents)
    fl=f.readlines()
    for i in fl:
      print(i)

if __name__ == "__main__":
  main()
