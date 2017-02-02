import os
from random import randint

def getUserPoint(userName):
    try:
        f = open('userScores.txt', 'r')
    except IOError as e:
        f = open('userScores.txt', 'w')
        f.close()
        return '-1'

    index = -1
    point = 0
    for line in f:
        nameLine = line.split(', ')
        index = nameLine[0].find(userName)
        if (index > -1):
            point = nameLine[1]
            break;
    f.close()
    return point if index >  -1 else '-1'

'''
    newUser: can either be True or False.
'''
def updateUserPoints(newUser, userName, score):
    if (newUser):
        f = open('userScores.txt', 'a')
        score = "\n%s, %d" %(userName, score)
        f.write(score)
        f.close()
    else:
        tmp = open('userScores.tmp', 'w')
        f = open('userScores.txt', 'r')

        for line in f:
            if (line.split(', ')[0] == userName):
                line = "{}, {}".format(userName, score)
            tmp.write(line)
        tmp.close()
        f.close()

        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')

'''
'''
def generateQuestion():
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}

    for i in range(0,5):
        operandList[i] = randint(1, 9)
    # print operandList

    lastOprator = ''
    for i  in range(0, 4):
        if (lastOprator == '**'):
            lastOprator = operatorDict[randint(1, 3)]
        else:
            lastOprator = operatorDict[randint(1, 4)]
        operatorList[i] = lastOprator
    # print operatorList

    operatorCount = len(operatorList)
    questionString = ''
    for i in range(0, operatorCount):
        questionString = questionString + str(operandList[i])
        questionString = questionString + operatorList[i]
    questionString = questionString + str(operandList[operatorCount])
    # print(questionString)

    # result = eval(questionString)
    # print(result)

    # Step 1: Displaying the question to the user
    print(questionString.replace('**', '^'))

    # Step 2: Prompting the user for an answer
    answer = 0

    while True:
        answer = raw_input("Your answer is: ")
        try:
            answer = int(answer)
            break
            # return user score based on the answer
        except Exception:
            continue

    # Step 3: Evaluating the answer, displaying the appropriate message and returning the user's score.
    if (answer == eval(questionString)):
        print('Great!Go on?')
        return randint(1, 5);
    else:
        print('Come on, just do it!')
        return 0

#points = getUserPoint('John')
#print(points,)

#points = getUserPoint('Carol')
#print points,

# updateUserPoints(True, 'John', 200)

#updateUserPoints(False, 'John', 1001)
