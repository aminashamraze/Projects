print("Welcome to Arduino general knowledge quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Select true and false for following statements! ")
score = 0

answer = input("Arduino is an open-source electronics platform based on easy-to-use hardware and software.")

if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The brain of Arduino is called microcontroller. ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" IDE stands for Integrated Decentralized Environment. ")
if answer.lower() == "false":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The Arduino IDE is where you write and apply the code. ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Analog pins read analog signals and convert to digital value. ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

    answer = input("Some digital pins can simulate analog output using PWM. ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")
