# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
# book_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
# book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
# book_info = "charles dickens ; a tale of two cities ; 1859 ; ISN 978-0-14-143960-0 ; 544 ; 2299"
book_info = "j.k. rowling ;  harry potter and the sorcerer's stone   ; 1997 ; ISN 978-0-590-35340-3 ; 309 ; 3499.997"


book_info = book_info.split(" ; ")
print(book_info)
author, book_title, year_published, isbn, no_of_pages, cost = book_info
# author = book_info[0]
# book_title = book_info[1]
# year_Published = book_info[2]
# isbn = book_info[3]
# no_of_pages = book_info[4]
# cost = book_info[5]
# num = 9.56755
# print("{0:.3f}".format(num))




# print("author", author)
# print("book_title", book_title)
# print("year_Published", year_published)
# print("isbn", isbn)
# print("no_of_pages", no_of_pages)
# print("cost", cost)

author = author.title()
book_title = book_title.title().strip()
isbn = isbn.replace("ISN",'ISBN') 
# print(isbn)
# print(cost)
cost = float(cost)
cost = "{0:.2f}".format(cost)
cost = f"#{cost}"
# cost = "#" + cost
print(cost)
# print(type(cost))

book_information= f"The book {book_title} was written by {author} and published in {year_published}.It has {no_of_pages} pages and {isbn} and costs {cost}."
print(book_information)





