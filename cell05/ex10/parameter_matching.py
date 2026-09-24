import sys

if len(sys.argv) == 2:
    param = sys.argv[1]

    message = input("What was the parameter? ")
    
    if message == param:
        print("Good Job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
