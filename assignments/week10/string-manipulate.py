"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""
def is_vowel(char):
    return char.lower() in "aeiou"

def character_analysis(text):
    total_with_spaces = len(text)
    total_without_spaces = len(text.replace(" ", ""))

    vowels = [char for char in text if is_vowel(char)]
    consonants = [char for char in text if char.isalpha() and not is_vowel(char)]

    char_freq = {}
    for char in text.replace(" ", "").lower():
        char_freq[char] = char_freq.get(char, 0) + 1

    most_frequent_char = max(char_freq, key=char_freq.get)
    most_freq_count = char_freq[most_frequent_char]

    return {
        "total_with_spaces": total_with_spaces,
        "total_without_spaces": total_without_spaces,
        "vowels": vowels,
        "vowel_count": len(vowels),
        "consonant_count": len(consonants),
        "most_frequent_char": most_frequent_char,
        "most_freq_count": most_freq_count
    }

def word_analysis(text):
    words = text.split()
    total_words = len(words)
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    vowels_start = [word for word in words if word[0].lower() in "aeiou"]
    consonants_start = [word for word in words if word[0].lower() not in "aeiou"]

    return {
        "total_words": total_words,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "vowel_start_count": len(vowels_start),
        "consonant_start_count": len(consonants_start),
        "vowel_start_words": vowels_start,
        "consonant_start_words": consonants_start
    }

def string_transformations(text):
    title_case = text.title()
    upper_case = text.upper()
    lower_case = text.lower()
    acronym = ''.join(word[0].upper() for word in text.split() if word)
    reversed_text = text[::-1]
    reversed_words = ' '.join(word[::-1] for word in text.split())

    return {
        "title_case": title_case,
        "upper_case": upper_case,
        "lower_case": lower_case,
        "acronym": acronym,
        "reversed_text": reversed_text,
        "words_reversed": reversed_words
    }

# === MAIN PROGRAM ===
text = input("Enter text: ").strip()

# Perform analyses
char_info = character_analysis(text)
word_info = word_analysis(text)
transform_info = string_transformations(text)

# === REPORT ===
print("\n=== TEXT ANALYSIS REPORT ===")

# Character Analysis
print("Character Analysis:")
print("- Total characters: {} (with spaces), {} (without spaces)".format(
    char_info['total_with_spaces'], char_info['total_without_spaces']))
print("- Vowels: {} ({})".format(char_info['vowel_count'], ', '.join(char_info['vowels'])))
print("- Consonants: {}".format(char_info['consonant_count']))
print("- Most frequent: '{}' (appears {} times)".format(
    char_info['most_frequent_char'], char_info['most_freq_count']))

# Word Analysis
print("\nWord Analysis:")
print("- Total words: {}".format(word_info['total_words']))
print("- Longest word: \"{}\" ({} letters)".format(
    word_info['longest_word'], len(word_info['longest_word'])))
print("- Shortest word: \"{}\" ({} letters)".format(
    word_info['shortest_word'], len(word_info['shortest_word'])))
print("- Words starting with vowels: {} ({})".format(
    word_info['vowel_start_count'], ', '.join(word_info['vowel_start_words'])))
print("- Words starting with consonants: {} ({})".format(
    word_info['consonant_start_count'], ', '.join(word_info['consonant_start_words'])))

# Transformations
print("\nTransformations:")
print("- Title Case: {}".format(transform_info['title_case']))
print("- Upper Case: {}".format(transform_info['upper_case']))
print("- Lower Case: {}".format(transform_info['lower_case']))
print("- Acronym: {}".format(transform_info['acronym']))
print("- Reversed Text: {}".format(transform_info['reversed_text']))
print("- Words Reversed: {}".format(transform_info['words_reversed']))
