from tkinter import Y


print('Welcome to my computer quiz!')

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok! Let's play!")
score = 0
wrong = 0

answer = input("What does AWS stand for? ")
if answer.lower() == "amazon web services":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

answer = input("What is is the AWS Kubernetes acronym? ")
if answer.lower() == "eks":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

answer = input("What does ELB stand for? ")
if answer.lower() == "elastic load balancer":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")
    wrong += 1

answer = input("Which service enables infrastructure as code? ")
if answer.lower() == "cloud formation":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

print("You got " + str(score) + " questions correct out of " + str(score + wrong) +" questions!")
print("You got " + str(score / (score + wrong) * 100) + "%")