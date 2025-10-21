# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)def word_seperator():
    sentence = input("Enter a sentence where the first letter " \
    "of each word is all uppercase, but there are no spaces: ")
    result = ""
    for i, character in enumerate(sentence):
        if character.isupper() and i != 0:
            result += " "
        result += character 
    result = result.capitalize()
    return result 


print(word_seperator())