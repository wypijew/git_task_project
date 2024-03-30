'''
input_string = input("Enter a string: ")
result = "" # an empty string

for i, char in enumerate(input_string):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()

print("Result:", result)

input_string = input("Enter a string: ")
words = input_string.split() # change a string into a list of words
result_words = [] # empty list for the words with alternate cases

for i, word in enumerate(words):
    if i % 2 == 0:
        result_words.append(word.lower())
    else:
        result_words.append(word.upper())

result_string = ' '.join(result_words) # join the words in to a single string
print("Result:", result_string) 
'''
# Changes implemented to improve code readability and maintainability by encapsulating logic into reusable functions.

def alternate_case_string(input_string):
    # Convert characters in the input string to alternate upper and lower case.
    
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_string):
    # Convert words in the input string to alternate lower and upper case.
    
    words = input_string.split()
    result_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result_words.append(word.lower())
        else:
            result_words.append(word.upper())
    return ' '.join(result_words)

if __name__ == "__main__":
    # "Main" calls functions and prints their results when the script is executed directly.
 
    input_string = input("Enter a string: ")
    print("Result (alternate case characters):", alternate_case_string(input_string))
    
    input_string = input("Enter a string: ")
    print("Result (alternate case words):", alternate_case_words(input_string))
