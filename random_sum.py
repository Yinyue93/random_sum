import random
  
def random_calculation():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(number1 + number2)
    while True:
        if input(f"Calculate: {number1} + {number2} = ") == result:
            print("Correct!")
            break
        else:
            print("Incorrect.  Try again.")
 
random_calculation()

while input("New calculation? (Y/N) ") == "Y":
    random_calculation()  