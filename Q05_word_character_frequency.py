text = input("Enter a text: ")

words = text.split()

word_frequency = {}
character_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

for char in text:
    if char != " ":
        character_frequency[char] = character_frequency.get(char, 0) + 1

print("\nWord frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)

print("\nCharacter frequency:")
for char, count in character_frequency.items():
    print(char, ":", count)