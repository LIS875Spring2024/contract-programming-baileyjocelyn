import random

def flashcard_set(question,answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Nice job!")
        return True
    else:
        print("Please try again!")
        return False
    
def main():
    questions = [
        ("Flashcard 1: What word means to concent to recieve a thing offered? Accept or Except?", "Accept"),
        ("Flashcard 2: What word describes something you eat after a main course during a sit down dinner? Dessert or Desert?", "Dessert"),
        ("Flashcard 3: What word describes something that is first in order of importance or is related to money? Principle or Principal?", "Principal"),
        ("Flashcard 4: What word means to remove doubt or reassuure someone? Ensure or Assure?", "Assure"),
        ("Flashcard 5: What word describes employees at a company? Personnel or Personal?", "Personnel"),
    ]

    score = 0
    for question, answer in questions:
        if flashcard_set(question, answer):
            score += 1

    print("Nice work! You got", score,"flashcards correct!")

if __name__=="__main__":
    main()