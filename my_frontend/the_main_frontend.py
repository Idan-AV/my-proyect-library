import datetime
import os
import pickle

from my_backend.main_library import Library

library = None
if os.path.exists('library.pickle'):
    with open('library.pickle', 'rb') as f:
        library = pickle.load(f)
else:
    library_name = input("hi please enter your library name ")
    library = Library(library_name)

try:
    menu = """
    hi welcome to my library system!!
    to add a new customer please enter 1
    to add a new book please press 2
    to loan a book please press 3
    to return a book please enter 4
    to display all the books please enter 5
    to display all the customers enter 6
    to display all the loans please press 7
    to display all the late loans please enter 8 
    to display a loan for a specific customer please enter 9
    to find a book by name please enter 10
    to find a book by author please enter 11
    to find a customer by name please enter 12
    to remove a book please enter 13
    to remove a customer please enter 14
    to exit please enter 15
    thanks for choosing us as your partners!!!
    """
    while True:
        print(menu)
        your_choice = int(input("please enter your choice"))
        match your_choice:
            case 1:
                customer_id = int(input("please enter your id"))
                name = input("please enter your name")
                address = input("please enter your address ")
                email1 = input("please enter your email")
                your_birth_date = input("please enter your birth date in this format: yy-mm-dd")
                date_time = datetime.datetime.strptime(your_birth_date, "%Y-%m-%d")
                library.add_new_customer(customer_id, name, address, email1, date_time)
            case 2:
                book_id = int(input("please enter a book id "))
                name_of_the_book = input("please enter the book name")
                author = input("please enter the author's name")
                year_published = int(input("please enter the year that the book was published"))
                type_of_book = int(input("please enter the type of the book"))
                if type_of_book == 1 or type_of_book == 2 or type_of_book == 3:
                    library.add_a_new_book(book_id, name_of_the_book, author, year_published, type_of_book)
                else:
                    raise Exception("you inserted a type of book that does not exist ")
            case 3:
                customer_id = int(input("please enter your id"))
                book_id = int(input("please enter a book id "))
                type_of_book = int(input("please enter the type of the book"))
                if type_of_book == 1 or type_of_book == 2 or type_of_book == 3:
                    loan_date_str = input("please enter the loan date in this format: yy-mm-dd")
                    loan_date_1 = datetime.datetime.strptime(loan_date_str, "%Y-%m-%d")
                    is_available = bool(input("please insert True if the book is available or False if not "))
                    library.loan_a_book(customer_id, book_id, type_of_book, loan_date_1, is_available)
                else:
                    raise Exception("you inserted a type of book that does not exist ")
            case 4:
                customer_id = int(input("please enter your id"))
                book_id = int(input("please enter a book id "))
                return_book_date_str = input("please enter the return date in this format: yy-mm-dd")
                return_book_date = datetime.datetime.strptime(return_book_date_str, "%Y-%m-%d")
                library.return_a_book(customer_id, book_id, return_book_date)
            case 5:
                print(library.display_all_books())
            case 6:
                print(library.display_all_customers())
            case 7:
                print(library.display_all_the_loans())
            case 8:
                print(library.display_all_late_loans())
            case 9:
                customer_id = int(input("please enter your id"))
                print(library.display_loan_for_a_specific_person(customer_id))
            case 10:
                book_id = int(input("please enter a book id "))
                name_of_the_book = input("please enter the book name")
                print(library.find_book_by_name(book_id, name_of_the_book))
            case 11:
                book_id = int(input("please enter a book id "))
                author = input("please enter the author's name")
                print(library.find_book_by_author(book_id, author))
            case 12:
                customer_id = int(input("please enter your id"))
                name = input("please enter your name")
                print(library.find_customer_by_name(customer_id,name))
            case 13:
                book_id = int(input("please enter a book id "))
                library.remove_a_book(book_id)
            case 14:
                customer_id = int(input("please enter your id"))
                library.remove_customer(customer_id)
            case 15:
                break


except:
    print("error occurred, saving and exiting")
finally:
    with open('library.pickle', 'wb') as f:
        pickle.dump(library, f)
