import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {data["letter"]:data["code"] for (_, data) in data.iterrows()}
word = input("Enter a word: ").upper()
try:
    spelled_word = [data_dict[letter] for letter in word]
    print(spelled_word)
except KeyError:
    print(f"You entered some unwanted symbols or numbers in word: {word}")

