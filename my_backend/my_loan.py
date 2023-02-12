import datetime
from my_backend.my_book import Book


class Loan:
    def __init__(self, customer_id: int, book_id: int, book_type: int, loan_date: datetime, return_date: datetime,
                 is_book_available: bool = True):
        self._book_type = book_type
        self._is_book_available = is_book_available
        self._return_date = return_date
        self._loan_date = loan_date
        self._book_id = book_id
        self._customer_id = customer_id

    def get_customer_id(self):
        return self._customer_id

    def set_return_date(self, return_date2):
        self._return_date = return_date2

    def get_book_id(self):
        return self._book_id

    def loan_a_book(self):
        if self._is_book_available:
            self._loan_date = datetime.datetime.now()
            self._is_book_available = False

    def get_return_book_date(self):
        return self._return_date

    def calculate_amount_of_time_of_a_loan(self):
        return self._return_date - self._loan_date

    def return_a_book(self):
        if not self._is_book_available:
            self._is_book_available = True
            self._return_date = self._loan_date + self.calculate_amount_of_time_of_a_loan()

    def get_status_book(self):
        return self._is_book_available

    def type_of_loan_by_book(self):
        return self._book_type

    def __str__(self):
        return f"<customer id: {self._customer_id} and book id: {self._book_id},loan date: {self._loan_date} , " \
               f"return date: {self._return_date}  is the book available: {self._is_book_available}  >"

    def __repr__(self):
        return self.__str__()
