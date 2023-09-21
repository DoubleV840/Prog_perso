# -*- coding: utf-8 -*-
#Created by Willipatafoul at 20:24 on 17/05/2023
#

questions = {"Qui a créé python ?: ": "A",
                 "En quelle année à été créé python": "B",
                 "Python fait partie de quelle groupe comique ?": "C",
                 "La terre est elle ronde ?": "A"}
options = [["A: Guido van Rossum", "B: Elon Musk", "C: Bill Gates", "D: Mark Zuckerburg"],
            ["A: 1989", "B: 1991", "C: 2000", "D: 2016"],
            ["A: Lonely Island", "B: Smosh", "C: Monty Python", "D: SNL"],
            ["A: True", "B: False", "C: Sometimes", "D: C'est quoi la Terre ?"]]
    

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    print("**********************")
    print("BIENVENUE DANS LE QUIZ")
    print("**********************")
    print("Voici la première question :")
    
    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C or D: ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Not correct !")
        return 0
    
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("Resultats")
    print("----------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = correct_guesses/len(questions)*100
    print(f"Your score is : {score}%")
    
def play_again():
    reponse = input("Do you want to play again ? (yes/no)").lower()
    
    if reponse == "yes" or reponse == "y":
        return True
    else:
        return False
    
def main():
    new_game()
    while play_again():
        new_game()
    print("Ok bye !")
    
if __name__ == '__main__':
    main()