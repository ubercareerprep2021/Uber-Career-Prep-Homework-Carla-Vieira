import pytest
from trees.ex5 import ListPhoneBook, BinarySearchTreePhoneBook


class TestListPhoneBook:

    def setup_method(self):
        self.list_phonebook = ListPhoneBook()
        self.list_phonebook.insert("ABC", 1111111111)
        self.list_phonebook.insert("XYZ", 9999999999)
        self.list_phonebook.insert("DEF", 2222222222)

    def test_size(self):
        assert self.list_phonebook.size() == 3

    def test_find(self):
        assert self.list_phonebook.find("ABC") == 1111111111
        assert self.list_phonebook.find("XYZ") == 9999999999
        assert self.list_phonebook.find("PQR") == -1

class TestBSTPhoneBook:

    def setup_method(self):
        self.bst_phonebook = BinarySearchTreePhoneBook()
        self.bst_phonebook.insert("ABC", 1111111111)
        self.bst_phonebook.insert("XYZ", 9999999999)
        self.bst_phonebook.insert("DEF", 2222222222)

    def test_size(self):
        assert self.bst_phonebook.size() == 3

    def test_find(self):
        assert self.bst_phonebook.find("ABC") == 1111111111
        assert self.bst_phonebook.find("XYZ") == 9999999999
        assert self.bst_phonebook.find("PQR") == -1