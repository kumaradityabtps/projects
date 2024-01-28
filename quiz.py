print("Welcome to computer quiz!")

playing = input("do u want to play? ")

if playing.lower() != "yes":
    quit()
    
print("okay! Lets play :) y")
score=0


answer = input("What does the Cpu stands for?")
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("what does gpu stands for?")
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("what does ram stannds for?")
if answer == "random only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

yesanswer = input("what does psu stands for?")
if answer == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
print("you got" +str(score) + "questions correct!")
    
    
    