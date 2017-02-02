def checkIfPrime(numberToCheck):
    for number in range(2,numberToCheck):
        if (numberToCheck%number == 0):
            return False
    return True

answer = checkIfPrime(13)

print answer
