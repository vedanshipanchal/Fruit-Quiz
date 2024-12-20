import random

class fruitquiz:
    def __init__(self):
        self.fruit = { 'banana': 'yellow',
                        'apple': 'green',
                        'dragon fruit': 'pink',
                        'watermelon': 'red',}
    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruit.items()))
            print("What is the color of the",fruit)
            user = input("Enter answer right now!!!!!")
            if user.lower() == color:
                print("correct answer good job!!!!!")
            else:
                print("wrong answer go to detention right now!!")
                option = int(input("1-stop, 0-continue"))
                if option:
                    break

fq = fruitquiz()
fq.quiz()