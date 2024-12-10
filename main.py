def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)

    char_count = count_characters(file_contents)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    dictionaries = []
    for char, count in char_count.items():
        dictionaries.append({"char": char, "count": count})
    sorted_chars = sorted(dictionaries, key=sort_on, reverse=True)
    for sort in sorted_chars:
        char = sort["char"]
        count = sort["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


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

def sort_on(dictionary):
    return dictionary["count"]

main()
