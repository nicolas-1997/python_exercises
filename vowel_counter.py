def vowel_counter(word):
    vowels = ["a", "e", "i", "o", "u"]
    number_of_vowels = 0
    
    for x in word:
        if x in vowels:
            number_of_vowels += 1
    
    return number_of_vowels

def run():
    word = input("Enter a word: ")

    result = vowel_counter(word)
    print(f'{result} vowels were found in your word {word}')

if __name__ == "__main__":
    run()