def main():
    print("--- Begin report of books/frankenstein.txt ---")
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Count words
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    
    # Count characters
    num_characters = character_count_lowercase(text)
    
    # Sort characters by count in descending order
    sorted_characters = sorted(num_characters.items(), key=lambda x: x[1], reverse=True)
    
    # Print sorted character counts
    for character, count in sorted_characters:
        print(f"The '{character}' character was found {count} times")
    
    print("--- End report ---")


def word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def character_count_lowercase(text):
    lowered_string = text.lower()
    character_count = {}
    for character in lowered_string:
        if character.isalpha():  # Only count alphabetic characters
            character_count[character] = character_count.get(character, 0) + 1
    return character_count


main()