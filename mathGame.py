import myPythonFunctions as m

userName = raw_input('Please enter your name: ')

scoreText = m.getUserPoint(userName)
userScore = int(scoreText)

newUser = True if userScore==-1 else False

if (newUser):
    print("Welcome to math game world!")
    userScore = 0
else:
    print("Hi, %s. Your score is %d" %(userName, userScore))

userChoice = '0'
while userChoice != "-1":
    # generate a new question
    score = m.generateQuestion()
    userScore = userScore + score
    print("Your current score is %d" %(userScore))

    userChoice = raw_input("Continue?")

m.updateUserPoints(newUser, userName, userScore)

print("Bye!")
