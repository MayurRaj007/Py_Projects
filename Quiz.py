print("Wellcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
num_of_questions = 4
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What is www stand for? ")
if answer.lower() == "world wide web" :
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit" :
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

print("You got " + str(score) + " of " + str(num_of_questions) + " questions corrct!")
print("Your score is: " + str((score / num_of_questions) * 100) + " %.")
