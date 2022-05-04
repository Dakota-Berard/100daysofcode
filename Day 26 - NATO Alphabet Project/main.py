student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")



alpha_dict = {row.letter:row.code for (index, row) in alpha_data.iterrows()}
print(alpha_dict)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phrase = input("What word would you like to relay? ")

list_response = [alpha_dict.get(n.upper()) for n in phrase]

print(list_response)