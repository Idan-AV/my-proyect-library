import datetime
import unittest

from my_backend.main_library import Library
from my_backend.my_book import Book
from my_backend.my_customer import Customer
from my_backend.my_loan import Loan


class LibraryTestCase(unittest.TestCase):
    def test_something1(self):
        library = Library("my_library")
        library.add_new_customer(123, "idan", "lod", "bla", datetime.date(year=2005, month=11, day=12))
        library.add_a_new_book(344, "venom", "tom", 1999, 1)
        library.loan_a_book(123, 344, 1, datetime.datetime(year=2023, month=1, day=7), True)
        loan = Loan(123, 344, 1, datetime.datetime(year=2023, month=1, day=7), 0)
        library.return_a_book(123, 344, datetime.datetime(year=2023, month=2, day=7))
        self.assertTrue(loan.get_status_book())

    def test_somthing2(self):
        customer = Customer(123, "idan", "lod", "bla", datetime.date(year=2005, month=11, day=12))
        self.assertEqual(customer.get_name(), "idan")
        self.assertEqual(customer.get_customer_id(), 123)
        self.assertEqual(customer.get_address(), "lod")
        self.assertEqual(customer.get_birth_date(), datetime.date(year=2005, month=11, day=12))

    def test_somthing3(self):
        book = Book(12345, "venom", "toby", 1987, 1)
        self.assertEqual(book.get_book_id(), 12345)
        self.assertEqual(book.get_name(), "venom")
        self.assertEqual(book.get_type_of_book(), 1)
        self.assertEqual(book.get_author(), "toby")


if __name__ == '__main__':
    unittest.main()
