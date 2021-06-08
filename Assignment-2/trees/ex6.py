import csv
import time

from ex5 import ListPhoneBook, BinarySearchTreePhoneBook


def insert_data(phonebook):
    for contact in contacts:
        phonebook.insert(contact["name"], contact["phone_number"])

def search(phonebook):
    for search in searches:
        phonebook.find(search)

def get_data_from_csv(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        contacts = []
        for row in csv_reader:
            contacts.append({"name": row[0],
            "phone_number": row[1]
            })
    return contacts

def get_data_from_txt(file_name):
    with open(file_name) as txt_file:
        searches = []
        for row in txt_file:
            searches.append(row)
    return searches

def print_report(phonebook):
    start_insert = time.time()
    insert_data(phonebook)
    end_insert = time.time()
    print(f"Insert took {int((end_insert-start_insert)*1000)} milliseconds.")
    print(f"The size of the PhoneBook is {phonebook.size()}")
    print(f"find() was called {len(searches)} times.")
    start_search = time.time()
    search(phonebook)
    end_search = time.time()
    print(f"Search took {int((end_search-start_search)*1000)} milliseconds.")

if __name__ == '__main__':
    contacts = get_data_from_csv("inputs/data.csv")
    searches = get_data_from_txt("inputs/search.txt")
    print("** Report for List **")
    print_report(ListPhoneBook())
    print("\n** Report for Binary Search Tree **")
    print_report(BinarySearchTreePhoneBook())


