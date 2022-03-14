#
# Example file for working with date information
#
from datetime import date,time,datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  # today=date.today()
  # print("Today's date is : ", date.today())

  # # print out the date's individual components
  # print("Date components are : ",today.day,today.month,today.year)
    
  # # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("Weekday no is : ",today.weekday())
  # day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  # print("which is : ", day[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("Current date and time is : ", datetime.now())
  
  # Get the current time
  t=datetime.time(datetime.now())
  print(t)

 

  
if __name__ == "__main__":
  main();
  