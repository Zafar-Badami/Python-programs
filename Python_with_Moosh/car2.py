from http.client import responses
from urllib import response
response=""
car_started=False

while True:
    response=input(" > ").upper()
    
    if response == "HELP":
        print("""
start - to start the car
stop  - to stop the car
quit  - to exit
        """)
    elif response == "START":
        if car_started == False:
            car_started = True
            print("Car started...")
        else:
            print("Car already started...")
    elif response == "STOP":
        if car_started == True:
            car_started = False
            print("Car stopped")
        else:
            print("Car already stopped....")
    elif response == "QUIT":
        break
        
    else:
        print("I don't understand...")