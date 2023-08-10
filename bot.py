from collections import UserDict


class Field:  # буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів
    pass


class Name:  # обов'язкове поле з ім'ям
    def __init__(self, name) -> None:
        self.name = name

    def add_name(self):
        self.name = input("Enter your name: ")


class AdressBook(UserDict):  # додамо логіку пошуку за записами
    def find_record(self, value):
        return self.data.get(value)


class Record:  # відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    def add_record(self, record: Record):
        self.data[Record.name.value] = record


class Phone:  # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    def __init__(self, number=None) -> None:
        self.number = number
