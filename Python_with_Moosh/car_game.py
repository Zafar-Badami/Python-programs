command = " "
started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car already started...")
        else:
            started=True
            print("car started ......")

    elif command == 'stop':
        if not started:
            print("car already stopped")
        else:
            print("car stopped...")
            started=False
        
      
    elif command == "help":
        print("""
To start the car type 'start'
To stop the car type 'stop'
For help type 'help'
To quit the game type 'quit'
                """)
        
    elif command == "quit":
        break
    
    else:
        print("wrong input")
