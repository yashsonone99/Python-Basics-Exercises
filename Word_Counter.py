#Input text
input_text = "This is a sample text. This text will be used to demonstrate the word counter."
#Split the text into individual words
words = input_text.split()
#Create a dictionary to store word counts
word_count = {}
#loop through each word
for word in words:
#If the word is already in the dictionary then increase the count
    if word in word_count:
        word_count[word] += 1
    else:
        # If it's the first time we've seen the word then add it to the dictionary
        word_count[word] = 1
#Print the result.
for word, count in word_count.items():
    print(f"'{word}': {count}")
