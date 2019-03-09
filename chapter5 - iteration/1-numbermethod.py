def calculateNumbers():
    count = 0
    average = 0
    total = 0

    isRunning = True
    while isRunning:
        userInput = input("Enter a number: ")

        # Terminate
        if userInput == "done":
            isRunning = False
            continue

        # Input parsing
        try:
            nextNumber = int(userInput)
        except:
            print("Invalid input")
            continue
        
        # Operations
        count = count + 1
        total = total + nextNumber
        average = total / count

    # Finished... So now, print the results
    print(total, count, average)

calculateNumbers()