
# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)
# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.
# library = [
#     {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_published": 1956, "isbn": "7867-678-546-532", "available": True},
#     {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_published": 1956, "isbn": "7867-678-546-532", "available": True},
#     {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_published": 1956, "isbn": "7867-678-546-532", "available": True},
# ]

library = [
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year_published": 1956, "isbn": "786-535", "available": True},
    # {"title": "New School Physics", "author": "Scott", "year_published": 1977, "isbn": "678-546", "available": True},
    # {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year_published": 1956, "isbn": "532-434", "available": True},
]


def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author: ").strip()
    year_published = input("Enter the year published: ").strip()
    isbn = input("Enter the ISBN: ").strip()
    library.append({"title": title, "author": author, "year_published": year_published, "isbn": isbn, "available": True})
    return f"Book '{title}' by {author} has been added to the library successfully"


def view_books():
    print(library)


def updatebook():
    isbn_to_search = input("Enter the ISBN of the book you want to update: ").strip()
    title = input("Enter new title of the book: ").strip()
    author = input("Enter new author: ").strip()
    year_published = input("Enter new year published: ").strip()
    isbn = input("Enter the new ISBN: ").strip()

    for book in library:
        if book["isbn"] == isbn_to_search:
            book["title"] = title
            book["author"] = author
            book["year_published"] = year_published
            book["isbn"] = isbn
            book["available"] = True


def deletebook():
     isbn_to_search = input("Enter the ISBN of the book you want to delete: ").strip()
     for book in library:
        if book["isbn"] == isbn_to_search:
            del book


def search_book():
    title = input("Enter the title of the book you want to search: ").strip()
    for book in library:
        if title == book["title"]:
            print(book)
        else:
            print("opps book doesnt exist in our library")


def borrow_book():
     isbn_to_search = input("Enter the ISBN of the book that you want to borrow: ").strip()
     for book in library:
         if book["isbn"] == isbn_to_search:
             if book["available"]:
                 print("your request is approved please return on time")
                 book["available"] = False  
             else:
                 print(f"{book["title"]} is not available at the moment")


def return_book():
     isbn_to_search = input("Enter the ISBN of the book that you want to return: ").strip()
     for book in library:
         if book["isbn"] == isbn_to_search:
             if book["available"]:
                 print(f"{book["title"]} with ISBN {book["isbn"]} is already available in the library check the ISBN carefully")
             else:
                 book["available"] = True  
                 print(f"book title {book["title"]} with ISBN {book["isbn"]}Returned successfully")
                 
             
             

menu = """
***********************MENU*****************************
1. Add Book
2. View Book
3. Update book
4. delete book
5. search book
6. borrow_book
7 return_book
8. Exit

"""

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ")
    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "8":
        print("Exiting the library...")
        break
    elif choice == "3":
        updatebook()
    elif choice == "4":
        deletebook()
    elif choice == "5":
        search_book() 
    elif choice == "6":
        borrow_book()
    elif choice == "7":
        return_book()
    else:
        print("Invalid choice")
        continue
