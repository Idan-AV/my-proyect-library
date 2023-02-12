# from my_backend.my_address import Address
import datetime


class Customer:
    def __init__(self, customer_id: int, name: str, address: str, email: str, birth_date: datetime):
        self._birth_date = birth_date
        self._email = email
        self._address = address
        self._name = name
        self._customer_id = customer_id

    def get_customer_id(self):
        return self._customer_id

    def get_email(self):
        return self._email

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_birth_date(self):
        return self._birth_date

    def __str__(self):
        return f"<customer id: {self._customer_id} and customer name: {self._name},  customer's birth date: {self._birth_date} >"

    def __repr__(self):
        return self.__str__()
