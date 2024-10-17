"""
Write a program to count the occurrences of words in a string.
The program should ask the user for a string,
then print the counts of how many of each word are in the string.
"""
word_to_count = {}
text = input('Enter a string: ')
# my money your money my money your money i like you
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
#    print(f"{word}: {word_to_count[word]}")

# for printing only unique words with their counts
words = list(word_to_count.keys())
words.sort()
max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}}: {word_to_count[word]}")


