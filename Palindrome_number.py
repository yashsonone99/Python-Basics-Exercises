def is_palindrome(text):
    #Convert text to lowercase and remove spaces
    clean_text = ''.join(text.lower().split())
    #Reverse the text
    reversed_text = clean_text[::-1]
    #Compare and return result
    return clean_text == reversed_text
#Take input from the user
user_input = input("Enter a word or phrase: ")
#Check if it's a palindrome
if is_palindrome(user_input):
    print("Yes, It is a palindrome!")
else:
    print("No, It is not a palindrome.")
