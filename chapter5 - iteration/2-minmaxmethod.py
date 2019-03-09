def minMaxFromInput():
    count = 0
    minNumber = float("inf")
    maxNumber = float("-inf")

    isRunning = True
    while isRunning:
        userInput = input('Next Number: ')

        if userInput == 'done':
            isRunning = False
            continue

        # Input parsing
        try:
            nextNumber = float(userInput)
        except:
            print("Invalid input")
            continue
        
        if nextNumber < minNumber:
            minNumber = nextNumber
        if nextNumber > maxNumber:
            maxNumber = nextNumber
        count = count + 1

    print('Min: ' + str(minNumber), 'Max: ' + str(maxNumber), 'Number Count: ' + str(count))

minMaxFromInput()