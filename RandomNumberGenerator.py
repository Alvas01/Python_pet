import random

print("*" * 15, "Guess a number", "*" * 15)

score = 0
i = 0

while True:

    rand = random.randint(1, 10)
    answer = int(input("A number has been set between 1 and 10. Try to guess the number: "))
    
    if answer < 1 or answer > 10:
        print("No! The number must be between 1 and 10")
    elif answer == rand:
        score += 1
        print("Well done!")
        i +=1
        break
    else:
        print("Failure! Try again!")
        
    i += 1

print("Right answers: ", score, "out of", i)    
print("Come back again!")