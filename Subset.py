from itertools import combinations

while True:                                                                     #Take valid number input from user and keep the prompt running if the input is invalid.
    A = input("Enter the set of numbers(sepreate each number by space): ")
    try:
        A = list(map(int, A.split()))                                           #Check if all the of the user input are integers and turn them to a list.
        break
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")

while True:                                                                     #Check to see if the user wants to remove any duplicates present in the input.
    q = input("Do you want to remove duplicates(Y/N): ")
    if q.upper() == 'Y':
        A=set(A)                                                                #If the user wants to remove duplicates turn the list into set to remove duplicates.
        A=list(A)                                                               #Turns the set back into a list.
        print(f"Set of numbers(After removal of duplicates): {A}")              #Prints list of numbers A.
        break
    elif q.upper() == 'N':
        print(f"Set of numbers: {A}")                                           #Prints list of number A with duplicates.
        break
    else:
        print("Invalid input.")
        continue

while True:                                                                     #Take valid subset range input from the user and continues till correct input is deffined by the user.
    z = input("Enter subset size range (e.g., '3-5' or '4'): ")
    if '-' in z:                                                                #Checks if subset size is a range (contains -).
        parts = z.split('-')
        if len(parts) == 2 and all(p.strip().isdigit() for p in parts):         #Checks if the size range contains - is split in two and both parts are digits.
            x, y = sorted(map(int, parts))                                      #Transfers the range to x and y.
            break
        else:
            print("Invalid range. Use format like '3-5'.")                      #Invalid input message.
    elif z.strip().isdigit():                                                   #Checks if subset size is a single digit.
        x = y = int(z)                                                          #Transfers the value to x and y.
        break
    else:
        print("Invalid input. Enter a number or a range like '3-5' or '4'.")

while True:                                                                     #Prompts for user input till a correctc value is input.
    s = (input("Enter the requireed sum of the subset values: "))
    if s.strip().isdigit():                                                     #Checks if input value is an int.
        s=int(s)
        break
    else:
        print("Invalid input.")
        continue

while True:                                                                     #Prompts for user input till a correctc value is input.
    iter=(input("Enter the number of iterations to run: "))
    if iter.strip().isdigit():                                                  #Checks if input value is an int.
        iter=int(iter)
        break
    else:
        print("Invalid input.")
        continue

allvsubset = []                                                                 #Create a list of all valid subsets (allvsubset).

for i in range(x, y + 1):                                                       #Subset size range.
    for subset in combinations(A, i):                                           #Creates a subset from list A of size i. i is in range(x,y+1)
        if sum(subset) == s:                                                    #Checks if the sum of elements of subset is equal to required sum.
            allvsubset.append(subset)                                           #Adds subset to allvsubset.
            if len(allvsubset) >= iter-1:                                       #Checks if the number of all valid subset are under the amount of specified iterations.
                break


print(f"Total valid subsets: {len(allvsubset)}")                                #Prints number of all valid subsets (prints the number of iterations if all valid subset exceed the set number of iterations.)
print("[ ", end="")                                                             #Prints all valid subsets.
for subset in allvsubset:
    print(subset, end = ", ")
print("\b\b]")