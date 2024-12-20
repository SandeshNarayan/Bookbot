def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f'{count_words(file_contents)} words found in the document')
        char_count=count_chars(file_contents)
        for char in char_count:
            print(f'The {char} character was found {char_count[char]} times')

def count_words(text):
    words = text.split()

    return len(words)



def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

if __name__=="__main__":
    main()