import pandas

# Load the CSV file into a pandas DataFrame
data = pandas.read_csv("training-code/day_26/nato_phonetic_alphabet.csv")

# Create a dictionary where each letter is mapped to its corresponding phonetic code
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Prompt the user to enter a word
word = input("ENTER A WORD: ").upper()

# Generate a list of phonetic code words corresponding to the input word
output_list = [phonetic_dict[letter] for letter in word]

# Print the list of phonetic codes
print(output_list)
