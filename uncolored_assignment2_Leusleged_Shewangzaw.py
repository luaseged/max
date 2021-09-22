

name = input("Hello!, \nPlease Enter Your Name: ").capitalize()

print("Hello again " + name + "."
"\nWelcome! This is a simple imagination quiz.\n")
response = input("Do you wanna play the quiz?\nEnter 'Y' for Yes  or enter 'N' for No:\n").capitalize()

if response == "Y":
    print("Great! let's play then!")
    print("You have the following information. Please read them carefully.")

    print("***************************************************")
    print(" ***********************************************")
#Given
    print("Persons live in a street, having houses in line. Consider the following: ")
    print("    A lives in the corner’s house,             ")
    print("    C is between E and G,                      ")
    print("    There is 1 house between D and F,          ")
    print("    F is neighbor of G and,                    ")
    print("    There are two houses between A and G.      ")

    print(" ***********************************************")
    print("*************************************************")


    print("Based on the information given above answer the following questions.\nGood luck!!!\n")
    score = 0
    questions = 0

#Q1
    Q1 = input("1. Who lives in the second corner?\n   Your answer: ").capitalize()
    if Q1 == 'D':
        print("Correct! the answer is D")
        score += 1
        questions +=1
        print("your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    elif Q1 == "A" or Q1 == "A" or Q1 == "B" or Q1 == "C" or Q1 == "E" or Q1 == "F" or Q1 == "G":
        print("No! the correct answer is 'D'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print("Invalid answer.\nThe correct answer is 'D'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")


#Q2
    Q2 = input("2. Who lives in the middle?\n   Your answer: ").capitalize()
    if Q2 == 'G':
        print("Correct! the answer is G")
        score += 1
        questions +=1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q2 == "A" or Q2 == "A" or Q2 == "B" or Q2 == "C" or Q2 == "E" or Q2 == "F" or Q2 == "D":
        print("No! the correct answer is 'G'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print("Invalid answer.\nThe correct answer is 'G'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")

#Q3
    Q3 = input("3. Who lives between B and G?\n   Your answer: ").capitalize()
    if Q3 == 'F':
        print("Correct! the answer is F")
        score += 1
        questions +=1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q3 == "A" or Q3 == "A" or Q3 == "B" or Q3 == "C" or Q3 == "E" or Q3 == "G" or Q3 == "D":
        print("No! the correct answer is 'F'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print("Invalid answer.\nThe correct answer is 'F'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
#Q4
    Q4 = input("4. Who is the neighbor of A?\n   Your answer: ").capitalize()
    if Q4 == 'E':
        print("Correct! the answer is E")
        score += 1
        questions +=1
        print("your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    elif Q4 == "E" or Q4 == "A" or Q4 == "B" or Q4 == "C" or Q4 == "F" or Q4 == "G" or Q4 == "D":
        print("No! the correct answer is 'E'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    else:
        print("Invalid answer.\nThe correct answer is 'E'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")

#Q5
    Q5 = str(input("5. How many houses are there between B and E?\n   Your answer: "))
    if Q5 == '5':
        print("Correct! the answer is 5")
        score += 1
        questions +=1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q5 != "5":
        print("No! the correct answer is '5'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print("Invalid answer.\nThe correct answer is 'E'.")
        score += 0
        questions += 1
        print("your score is : " + str(score) + "/" + str(questions) +"\n\n")


    print("Dear " + name + ", your final score is: " + str(score) + "/" + str(questions))
    if score == 5:
        print("you are so good at imagination. Keep it up!!\nGood by dear " + name + ".")
    elif score >= 3 and score < 5:
        print("you are good, but good can be better.\nHere is the correct order of the houses: \nA>>E>>C>>G>>F>>B>>D.\n Good bye " + name +".")
    elif score >= 1 and score < 3:
        print("Exprience more dear " + name + ".\nHere is the correct order of the houses: \nA>>E>>C>>G>>F>>B>>D.\nGood bye for now.")
    else:
        print("Hmm, it seems that you don't understand the quiz.\nHere is the correct order of the houses: \nA>>E>>C>>G>>F>>B>>D. Good bye " + name +".")


elif response == "N":
    print("Okay, that is unfortunate! Good by!!")
    exit()
else:
    print("Ohh!!!, That is an invalid input.\nGood bye!!!")
    exit()