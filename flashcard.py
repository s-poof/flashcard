import time
import random

flashcards = {
    'what is 2 + 2': '4',
    'what is the capital of france': 'paris',
    'what year is it': '2025',
    'what color is the sky': 'blue'
}

#main quiz
def run_quiz(flashcards):
    total = len(flashcards)
    score = 0

    shuffled_cards = list(flashcards.items())
    random.shuffle(shuffled_cards)
    
    for question, answer in shuffled_cards:
        user = input(f"Q: {question}\n")
        if user.strip().lower() == answer:
            score += 1
            print('correct!')
        else:
            print(f'wrong. The correct answer is {answer}')


    percent = (score/total)*100

    print(f'You got an {percent}%')




while True:
    run_quiz(flashcards)

    time.sleep(1)

    again = input('Great job. Would you like to go again? (y/n)\n:')
    if again == 'y':
        time.sleep(1)
        print('OK!')
    elif again == 'n':
        print("Goodbye!")
        break