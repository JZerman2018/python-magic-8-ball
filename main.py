import requests
import random
import time
import sys

answers = ["Yes, it seems so", "The chances are high", "Without a doubt", "The odds are in your favor", 
"It is certain", "Most likely", "Outlook Good", "Reply hazy, try again later", "You wouldn't like the answer",
"Can't predict now", "My sources say no", "It doesn't look good", "It Doubtful", "Signs point to no", "Signs point to yes",
"Why would you ask that?", "Are you kidding me?", "You know the answer is No", "Of course"]

def question():
    question = input("Please ask your yes or no question of The Great 8 Ball!\n")
    print("Thinking...")
    time.sleep(3)
    print(random.choice(answers))

while True:
    question()
    repeat = input("Would you like to ask another question? (Y or N)")
    if not (repeat == "y" or repeat == "Y"):
        print("Come back later if you have more questions!")
        break