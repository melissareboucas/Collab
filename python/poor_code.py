import math

# Function x
#
# Takes in three string parameters and prints out the greeting
#
# First parameter serves as the title, second as the first name and second is the surname
#
def x(a, b, c):
    print("Hello, " + a + " " + b + " " + c)

def locateTopEven(arr):
    topEven = 0
    indexOfTopEven = 0
    for i in range(0, len(arr)):
        n = arr[i]
        if n > topEven and n % 2 == 0:
            topEven = n
            indexOfTopEven = i
    return indexOfTopEven

# Function evaluate_conditions
#
# Takes an integer and two boolean parameters.
#
# It checks if integer parameter is different from 0 and returns the XOR of the booleans
#
# Otherwise, returns false.
# 
# XOR table: https://en.wikipedia.org/wiki/Exclusive_or
def evaluate_conditions(a: bool, b: bool, c: int):
    return (a ^ b) if c !=0 else False

def print_stats(arr):
    
    length = len(arr)
    
    print("Length = " + str(length))

    sum = 0.0
    for i in range(0, len(arr)):
        sum += arr[i]

    print("Sum =  " + str(sum))

    n = float(len(arr))

    mean = sum / n

    print("Mean = "+str(mean))

    sorted = b(arr)

    median = 0

    if(len(sorted) % 2 == 1):
        median = sorted[math.floor(len(sorted) / 2)]
    else:
        median = (sorted[math.floor(len(sorted) / 2) - 1] + sorted[math.floor(len(sorted) / 2)]) / 2
    
    print("Median = " + str(median))

    mode = sorted[0]
    top_occurences = 0
    current_number = sorted[0]
    occurences = 0

    for i in range(0, len(sorted)):
        if sorted[i] == current_number:
            occurences +=  1
            if occurences > top_occurences:
                top_occurences = occurences
                mode = current_number
        else:
            current_number = sorted[i]
            occurences = 1
    
    print("Mode = " + str(mode))

    variance = 0

    for i in range(0, len(arr)):
        diff = arr[i] - mean
        variance += diff * diff
    variance /= length

    print("Variance = " + str(variance))

    standard_deviation = math.sqrt(variance)

    print("Standard Deviation = " + str(standard_deviation))

def b(arr):
    sorting_arr = arr.copy()
    for i in range(0, len(sorting_arr) - 1):
        for j in range(i + 1, len(sorting_arr)):
            if sorting_arr[i] > sorting_arr[j]:
                temp = sorting_arr[i]
                sorting_arr[i] = sorting_arr[j]
                sorting_arr[j] = temp
    return sorting_arr

# True for 2, 3, 5, 7, 11, 13 ...
# False for 1, 4, 6, 8, 9, 10, 12 ...
def p(n: int):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intArrayToString( inputArray ):
    outputString = "{"
    for i in range( 0, len( inputArray ) ):
        if i > 0:
            outputString = outputString + "; "
        outputString = outputString + str( inputArray[i] )
    outputString = outputString + "}"
    return outputString

# Big Sergio Comp8860 -> bIG sERGIO cOMP8860
def casing(s) :
    out = "" # Set out to be an empty string
    # Iterate through the string
    for i in range(0, len(s)):
        # Upeercase letters become lowercase letters
        if s[ i].upper() == s[i]:
            out = out +  s[i].lower()
        else:
            # And vice-versa
            if s[i].lower() == s[i]:
                out = out + s[i].upper()
            else:
                out = out +  s[i] ## TODO: add a comment explainting why we just copy the original letter here as it may be confusing to the next person trying to maintain the code
    return out # Return the out variable


def how_many(f: bool, t: bool, k: bool, z: bool):
    if f == True:
        if k == False:
            if z and t:
                return 3
            if z or t:
                return 2
            return 1
        else:
            if z == True:
                if t: return 4
                else: return 3
            if t == True:
                if z: return 4
                else: return 3
            else: return 2
    if k and t and z:
        return 3
    if k or z or t:
        number = 0
        if k and z: number  = number + 2
        else: 
            if z or k: number += 1
            number += 1 if t else 0
            return number
    return 0
