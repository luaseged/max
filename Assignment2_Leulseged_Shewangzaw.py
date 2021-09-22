import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


name = input(Fore.CYAN + Style.BRIGHT + "Hello!, \nPlease Enter Your Name: ").capitalize()

print(Fore.CYAN + Style.BRIGHT + "Hello again " + Fore.LIGHTGREEN_EX + Style.BRIGHT + name + Fore.CYAN+ Style.BRIGHT + "."
"\nWelcome! This is a simple imagination quiz.\n")
response = input((Fore.CYAN + Style.BRIGHT + "Do you wanna play the quiz?\nEnter" + Fore.GREEN + " 'Y' " + Fore.CYAN + Style.BRIGHT + "for"
+ Fore.GREEN + Style.BRIGHT+ " Yes" + Fore.CYAN + Style.BRIGHT+ " or enter " + Fore.RED +Style.BRIGHT+  "'N'" +Fore.CYAN + Style.BRIGHT +
" for" + Fore.RED +Style.BRIGHT+ " No:\n")).capitalize()

if response == "Y":
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Great! let's play then!")
    print(Fore.CYAN+ Style.BRIGHT + "You have the following information. Please read them carefully.")

    print(Fore.LIGHTRED_EX + "***************************************************")
    print(Fore.LIGHTRED_EX + " ***********************************************")
#Given

    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "    A lives in the corner’s house,             ")
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "    C is between E and G,                      ")
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "    There is 1 house between D and F,          ")
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "    F is neighbor of G and,                    ")
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "    There are two houses between A and G.      ")

    print(Fore.LIGHTRED_EX + " ***********************************************")
    print(Fore.LIGHTRED_EX + "*************************************************")


    print(Fore.CYAN+ Style.BRIGHT + "Based on the information given above answer the following questions.\nGood luck!!!\n")
    score = 0
    questions = 0

#Q1
    Q1 = input(Fore.BLUE+ Style.BRIGHT + "1. Who lives in the second corner?\n   Your answer: ").capitalize()
    if Q1 == 'D':
        print(Fore.GREEN+ Style.BRIGHT + "Correct! the answer is D")
        score += 1
        questions +=1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    elif Q1 == "A" or Q1 == "A" or Q1 == "B" or Q1 == "C" or Q1 == "E" or Q1 == "F" or Q1 == "G":
        print(Fore.RED + Style.BRIGHT + "No! the correct answer is 'D'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid answer.\nThe correct answer is 'D'.")
        score += 0
        questions += 1
        print(Fore.YELLOW + Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")


#Q2
    Q2 = input(Fore.BLUE+ Style.BRIGHT + "2. Who lives in the middle?\n   Your answer: ").capitalize()
    if Q2 == 'G':
        print(Fore.GREEN+ Style.BRIGHT + "Correct! the answer is G")
        score += 1
        questions +=1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q2 == "A" or Q2 == "A" or Q2 == "B" or Q2 == "C" or Q2 == "E" or Q2 == "F" or Q2 == "D":
        print(Fore.RED + Style.BRIGHT + "No! the correct answer is 'G'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid answer.\nThe correct answer is 'G'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")

#Q3
    Q3 = input(Fore.BLUE+ Style.BRIGHT + "3. Who lives between B and G?\n   Your answer: ").capitalize()
    if Q3 == 'F':
        print(Fore.GREEN+ Style.BRIGHT + "Correct! the answer is F")
        score += 1
        questions +=1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q3 == "A" or Q3 == "A" or Q3 == "B" or Q3 == "C" or Q3 == "E" or Q3 == "G" or Q3 == "D":
        print(Fore.RED + Style.BRIGHT + "No! the correct answer is 'F'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid answer.\nThe correct answer is 'F'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
#Q4
    Q4 = input(Fore.BLUE+ Style.BRIGHT + "4. Who is the neighbor of A?\n   Your answer: ").capitalize()
    if Q4 == 'E':
        print(Fore.GREEN+ Style.BRIGHT + "Correct! the answer is E")
        score += 1
        questions +=1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    elif Q4 == "E" or Q4 == "A" or Q4 == "B" or Q4 == "C" or Q4 == "F" or Q4 == "G" or Q4 == "D":
        print(Fore.RED + Style.BRIGHT + "No! the correct answer is 'E'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/"+ str(questions) +"\n\n")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid answer.\nThe correct answer is 'E'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")

#Q5
    Q5 = str(input(Fore.BLUE+ Style.BRIGHT + "5. How many houses are there between B and E?\n   Your answer: "))
    if Q5 == '5':
        print(Fore.GREEN+ Style.BRIGHT + "Correct! the answer is 5")
        score += 1
        questions +=1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    elif Q5 != "5":
        print(Fore.RED + Style.BRIGHT + "No! the correct answer is '5'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid answer.\nThe correct answer is 'E'.")
        score += 0
        questions += 1
        print(Fore.YELLOW+ Style.BRIGHT + "your score is : " + str(score) + "/" + str(questions) +"\n\n")


    print(Fore.BLUE + Style.BRIGHT + "Dear " +Fore.LIGHTGREEN_EX + Style.BRIGHT + name + ", your final score is: " +Fore.BLUE + Style.BRIGHT  + str(score) + "/" + str(questions))
    if score == 5:
        print(Fore.BLUE + Style.BRIGHT + "you are so good at imagination. Keep it up!!\nGood by dear " +Fore.LIGHTGREEN_EX + Style.BRIGHT  + name + ".")
    elif score >= 3 and score < 5:
        print(Fore.BLUE + Style.BRIGHT + "you are good, but good can be better. \nHere is the correct order of the houses: \n"+ Fore.LIGHTGREEN_EX + Style.BRIGHT + "A>>E>>C>>G>>F>>B>>D." + Fore.BLUE + Style.BRIGHT + "\nGood bye for now," +Fore.LIGHTGREEN_EX + Style.BRIGHT + name +".")
    elif score >= 1 and score < 3:
        print(Fore.BLUE + Style.BRIGHT + "Exprience more dear " +Fore.LIGHTGREEN_EX + Style.BRIGHT + name + ".\nHere is the correct order of the houses: \n" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "A>>E>>C>>G>>F>>B>>D." + Fore.BLUE + Style.BRIGHT + "\nGood bye for now.")
    else:
        print(Fore.BLUE + Style.BRIGHT + "Hmm, it seems that you don't understand the quiz.\nHere is the correct order of the houses: \n" + Fore.LIGHTGREEN_EX + Style.BRIGHT + "A>>E>>C>>G>>F>>B>>D.\n"+ Fore.BLUE + Style.BRIGHT + "Good bye " +Fore.LIGHTGREEN_EX + Style.BRIGHT + name +".")
#exit
    inp = input("Enter 'X' to exit: ")
    if inp == x:
        print("bye")
        exit()
elif response == "N":
    print(Fore.RED +Back.BLACK+ Style.BRIGHT +"Okay, that is unfortunate! Good by!!")
    exit()
else:
    print(Fore.RED +Back.BLACK+ Style.BRIGHT +"Ohh!!!, That is an invalid input.\nGood bye!!!")
    exit()