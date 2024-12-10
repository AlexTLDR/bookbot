def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print(f"The total number of words is {word_count}")
    char_count = count_characters(file_contents)
    print(char_count)



def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

main()
