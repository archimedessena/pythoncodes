# one seeking for help, start for to start the car, stop to stop the car, quit to exit, asd for i dont understand that
#>start car started ready to go, >stop car stopped > quit

command = ""
started = False
while command != "quit":
      command = input("> ").lower()
      if command == "start":
           if started:
                print("Car already started")
           else:
               started = True
               print("Car started")
      elif command == "Stop":
           if not started:
                print("Car is already stopped")
           else:
               started = False
               print("Car stopped")
      elif command == "help":
           print("""
        Start - to start car
        Stop - to stop car
        quit - to exit """)
      elif command == "quit":
        break
else:
    ("Sorry i dont understand")














