# Program 13.5: Word Frequency Counter
# KEYWORD EXPLANATION:
# .get(key, default) - Dictionary method returning value for key if key exists, otherwise default value.
# .strip() - Method removing specified trailing/leading punctuation marks.
# .lower() - Method converting text to lowercase.

text = input("Enter a sentence: ")
words = text.split()
word_freq = {}

for word in words:
    word_clean = word.strip(".,!?").lower()
    if word_clean:  # ignore empty entries caused by punctuation-only tokens
        word_freq[word_clean] = word_freq.get(word_clean, 0) + 1

print("Word Frequencies:")
for word, count in word_freq.items():
    print(f"'{word}': {count}")