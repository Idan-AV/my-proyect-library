import datetime

# from my_backend.my_address import Address
from my_backend.my_book import Book
from my_backend.my_customer import Customer
from my_backend.my_loan import Loan


class Library:
    def __init__(self, library_name: str):
        self._library_name = library_name
        self.customers: dict[int:Customer] = {}
        self.books: dict[int:Book] = {}
        self.loans: dict[int:[Loan]] = {}
        self.returns: dict[int:[Loan]] = {}

    def get_library_name(self):
        return self._library_name

    def add_new_customer(self, customer_id, name: str, address: str, email: str, birth_date: datetime):
        if customer_id in self.customers:
            raise Exception("sorry but your customer id is already exists ")
        new_customer = Customer(customer_id, name, address, email, birth_date)
        self.customers[customer_id] = new_customer

    def add_a_new_book(self, id_book, name: str, author: str, year_published: int, type_of_book: int):
        if id_book in self.books:
            raise Exception("sorry but this book id is already exists ")
        new_book = Book(id_book, name, author, year_published, type_of_book)
        self.books[id_book] = new_book

    def loan_a_book(self, customer_id: int, book_id: int, book_type: int, loan_date: datetime,
                    is_book_available: bool):
        if not is_book_available:
            raise Exception("sorry but this book is already taken")
        elif customer_id not in self.customers:
            raise Exception("it seems like you dont have an account please create one")
        elif book_id not in self.books:
            raise Exception("sorry but this book id does not exist ")
        if customer_id not in self.loans:
            self.loans[customer_id] = []
            your_loan = Loan(customer_id, book_id, book_type, loan_date=loan_date, return_date=0,
                             is_book_available=False)
            self.loans[customer_id].append(your_loan)
        else:
            more_loans_for_the_same_customer = Loan(customer_id, book_id, book_type,
                                                    loan_date=loan_date, return_date=0, is_book_available=False)
            self.loans[customer_id].append(more_loans_for_the_same_customer)

    def return_a_book(self, customer_id: int, book_id: int, return_book_date: datetime):
        for loan in self.loans[customer_id]:
            if loan.get_status_book():
                raise Exception("sorry but this book is not taken")
        if customer_id not in self.customers:
            raise Exception("it seems like you dont have an account please create one")
        elif book_id not in self.books:
            raise Exception("sorry but this book id does not exist ")
        # ask the teacher
        loan_idx_to_remove = []
        for i, loan in enumerate(self.loans[customer_id]):
            if loan.get_book_id() == book_id:
                loan.set_return_date(return_book_date)
                loan.return_a_book()
                if customer_id not in self.returns:
                    self.returns[customer_id] = []
                    self.returns[customer_id].append(loan)
                else:
                    self.returns[customer_id].append(loan)
                loan_idx_to_remove.append(i)
        loan_idx_to_remove.sort(reverse=True)
        for i in loan_idx_to_remove:
            self.loans[customer_id].pop(i)

    def display_all_books(self):
        return self.books

    def display_all_customers(self):
        return self.customers

    def display_all_the_loans(self):
        return self.loans

    def display_all_late_loans(self):
        # ask
        for returns in self.returns.values():
            for return1 in returns:
                if return1.type_of_loan_by_book() == 1 and return1.calculate_amount_of_time_of_a_loan() > datetime.timedelta(
                        days=10):
                    print(return1)
                elif return1.type_of_loan_by_book() == 2 and return1.calculate_amount_of_time_of_a_loan() > datetime.timedelta(
                        days=5):
                    print(return1)
                elif return1.type_of_loan_by_book() == 3 and return1.calculate_amount_of_time_of_a_loan() > datetime.timedelta(
                        days=2):
                    print(return1)

    def display_loan_for_a_specific_person(self, customer_id: int):
        for loan in self.loans[customer_id]:
            print(loan)

    def find_book_by_name(self, book_id: int, book_name: str):
        if book_id not in self.books:
            raise Exception("sorry but this book id does not exist ")
        for book in self.books.values():
            if book.get_name() == book_name.lower():
                print(book)
            else:
                raise Exception("you didn't insert the correct name")

    def find_book_by_author(self, book_id, author_name: str):
        if book_id not in self.books:
            raise Exception("sorry but this book id does not exist ")
        for book in self.books.values():
            if book.get_author() == author_name.lower():
                print(book)
            else:
                raise Exception("you didn't insert the correct name")

    def find_customer_by_name(self, customer_id: int, customer_name: str):
        if customer_id not in self.customers:
            raise Exception("it seems like you dont have an account please create one")
        for customer in self.customers.values():
            if customer.get_name() == customer_name.lower():
                print(customer)
            else:
                raise Exception("you didn't insert the correct name")

    def remove_a_book(self, book_id: int):
        if book_id not in self.books:
            raise Exception("sorry but this book id does not exist ")
        if self.returns=={}:
            raise Exception("it seems like there arent any books in the returns dict")
        for returns in self.returns.values():
            for return1 in returns:
                if return1.get_status_book() and return1.get_book_id() == book_id:
                    self.books.pop(book_id)
                else:
                    raise Exception('you cant remover a book that is taken')
        # if book_id not in self.returns:
        #     raise Exception('you cant remover a book that is taken')
        # else:
        #     self.books.pop(book_id)

    def remove_customer(self, customer_id: int):
            if customer_id not in self.customers:
                raise Exception("it seems like you dont have an account please create one")
            if customer_id not in self.returns:
                raise Exception("cant remove a customer who is in doubt")

            if customer_id in self.returns:
                self.customers.pop(customer_id)


if __name__ == '__main__':
    my_library = Library("new")
    # my_address = Address("israel", "lod", "tlamim", 43578, 7)
    my_library.add_new_customer(123, "idan", "tlv herzhel 2", "avulovidan@gmail.com",
                                datetime.date(year=2005, month=11, day=12))
    my_library.add_a_new_book(4536, "alice in wonder land", "someone", 1989, 1)
    my_library.loan_a_book(123, 4536, 1,datetime.datetime(year=2023, month=1, day=7), True)
    my_library.display_loan_for_a_specific_person(123)

    # print(my_library.loans)
    # print(my_library.customers)
    # print(my_library.books)
    # my_library.add_a_new_book(4555, "alice in wonder land", "someone", 1989, 1)
    my_library.return_a_book(123, 4536, datetime.datetime(year=2023, month=2, day=7))
    # my_library.loan_a_book(123, 4555, 1,datetime.datetime(year=2023, month=1, day=10), True)
    # my_library.return_a_book(123,4555, datetime.datetime(year=2023, month=2, day=10))
    # print(my_library.returns)

    # print(my_library.loans)
    # print(my_library.returns)
    # print(my_library.display_all_books())
    # print(my_library.display_all_customers())
    # print(my_library.display_all_the_loans())
    # print(my_library.display_all_late_loans())
    # print(my_library.display_all_late_loans())
    # print(my_library.display_loan_for_a_specific_person(123))
    # print(my_library.find_book_by_name(4536,"alice in wonder land"))
    # print(my_library.find_book_by_author(4536,"someone"))
    # print(my_library.find_customer_by_name(123,"idan"))
    # my_library.remove_a_book(4536)
    # print(my_library.books)
    # my_library.add_new_customer(111, "idan", my_address, "avulovidan@gmail.com",
    #                             datetime.date(year=2005, month=11, day=12))
    # my_library.add_a_new_book(3344, "alice in wonder land", "someone", 1989, 1)
    # my_library.loan_a_book(111, 3344, 1, datetime.datetime(year=2023, month=1, day=7), True)
    # my_library.return_a_book(111,3344, datetime.datetime(year=2023, month=2, day=7))
    # my_library.remove_customer(123)
    # print(my_library.customers)
    # my_library.remove_customer(111)
    # print(my_library.customers)
    #
