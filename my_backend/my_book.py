class Book:
    def __init__(self, id_book: int, name: str, author: str, year_published: int, type_of_book: int):
        self._type_of_book = type_of_book
        self._year_published = year_published
        self._author = author
        self._name = name
        self._id_book = id_book

    def get_book_id(self):
        return self._id_book

    def get_year_published(self):
        return self._year_published

    def get_author(self):
        return self._author

    def get_name(self):
        return self._name

    def get_type_of_book(self):
        return self._type_of_book

    def __str__(self):
        return f"<book id: {self._id_book} and book name: {self._name},author's name: {self._author} ,finally " \
               f"year published: {self._year_published} >"

    def __repr__(self):
        return self.__str__()
