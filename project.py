import random
import string
from typing import List

def generate_book():
    """
    Return 1 random book - list with 3 elements: author, title, page_number.
    """

    letters = string.ascii_lowercase

    author = ''.join(random.choice(letters) for i in range(3))
    title = ''.join(random.choice(letters) for i in range(5))
    page_number = random.randint(50, 99)

    return [author, title, page_number]


def check_book_in_libr_1_1(book: list, libr_lst: List[list]):
    """
    Check if book is in the library: return True and index or False and None
    """

    if book in libr_lst: 
        return True, libr_lst.index(book)
    return False, None


def remove_book_from_libr_1_1(book: list, libr_lst: List[list]):
    """
    Remove book if exists and print info 
    """

    print(f'Removing {book} from {libr_lst}')
    flag, ind = check_book_in_libr_1_1(book, libr_lst)

    if flag:
        libr_lst.pop(ind)
        print(f'Done: {libr_lst}')
    else:
        print(f'Book does not exist')

def libr_list_1_1():
    """
    Task 1.1
    """

    print('Task 1.1')

    libr_lst = []
    books = [generate_book() for _ in range(3)]

    for book in books:
        libr_lst.append(book)
    
    print(f'Library: {libr_lst}')
    book_in_lib = books[0]
    book_not_in_lib = generate_book()

    remove_book_from_libr_1_1(book_in_lib, libr_lst)
    remove_book_from_libr_1_1(book_not_in_lib, libr_lst)

    print(f'Returning {book_in_lib} to library')
    libr_lst.append(book_in_lib)
    print(f'Library: {libr_lst}\n')

def check_book_in_libr_1_2(book: list, libr_lst: List[list]):
    """
    Check if book is in the library: return True and index or False and None
    """

    for i, lst in enumerate(libr_lst):
        if lst[1] == book:
            return True, i
    
    return False, None


def remove_book_from_libr_1_2(book: list, libr_lst: List[list]):
    """
    Remove book if exists and print info 
    """

    print(f'Removing {book} from {libr_lst}')
    flag, ind = check_book_in_libr_1_2(book, libr_lst)

    if flag:
        libr_lst[ind][0] = False
        print(f'Done: {libr_lst}')
    else:
        print(f'Book does not exist')

def libr_list_1_2():
    """
    Task 1.2
    """

    print('Task 1.2')

    libr_lst = []
    books = [generate_book() for _ in range(3)]

    for book in books:
        libr_lst.append([True, book])
    
    print(f'Library: {libr_lst}')

    book_in_lib = books[0]
    book_not_in_lib = generate_book()

    remove_book_from_libr_1_2(book_in_lib, libr_lst)
    remove_book_from_libr_1_2(book_not_in_lib, libr_lst)

    print(f'Returning {book_in_lib} to library')
    
    _, ind = check_book_in_libr_1_2(book_in_lib, libr_lst)
    libr_lst[ind][0] = True
    print(f'Library: {libr_lst}')

if __name__ == "__main__":
    libr_list_1_1()
    libr_list_1_2()
    pass