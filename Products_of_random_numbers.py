import random 
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
print("What is product of ", num1 , num2)
uans = int(input("Enter your answer: "))
cans = num1 * num2
if uans == cans:
    print("Correct Answer")
else:
    print("Incorrect. The correct answer is", cans)