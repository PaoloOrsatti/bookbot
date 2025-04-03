# Get the text of the book
from stats import count_words, count_characters, sorted_list  
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents        

def main():
    #file_path = input("Enter the book FilePath: ")
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text) 
    ch_dict = count_characters(book_text)
    
    #print(f"{num_words} words found in the document")
    #print(ch_dict)
    
    new_list = sorted_list(ch_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in new_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    return

main()

