#Write a Python program that checks whether a given number is prime or not. 
#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

number = int(input("Enter a number: "))
if number > 1:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
else:
    print(number, "is not a prime number.")
