'''
Given a year of birth provided by the user, calculate and return the age of the user.
Requirements:
1. Use at least on function
2. Prompt the user for the year of birth
3. One of the functions should have one or more parameters

'''

def calculateage(currentYear, birthYear):

    age = currentYear - birthYear

    return age

print(calculateage(2021,2000))


'''
Promt a user to input thier values of CY and YOB.
'''

def calculateage(currentYear, birthYear):

    age = currentYear - birthYear

    return age

def userInputs():
    
    currentYear = int(input("Enter currentYear"))
    birthYear = int(input("Enter birthYear"))
    age = calculateage(currentYear, birthYear)

    print(age)

userInputs()
