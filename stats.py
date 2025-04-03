def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    book_text = book_text.lower()
    print(book_text)
    thisdict = {}
    for character in book_text: 
        thisdict[character] = thisdict.get(character, 0) + 1
    return thisdict

def sort_on(dict):
    return dict["count"]

def sorted_list(thisdict):
    new_list = []
    new_dict = {}

    for i in thisdict:
        new_dict = {"char": i, "count": thisdict.get(i)}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list






