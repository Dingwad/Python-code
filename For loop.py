numRange = int(input("Please enter how may numbers you wish to add "))
total = 0


while(numRange <=1 or numRange>7):
    numRange = int(input("Please enter how may numbers you wish to add "))

for num in range(numRange):
    inputString = "Enter a number " + str(num) + " "
    total += int(input(inputString))

print("Your answer is ", total)
