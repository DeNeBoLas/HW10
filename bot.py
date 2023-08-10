from collections import UserDict


class Field:  # буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів
    pass


class Name:  # обов'язкове поле з ім'ям
    def __init__(self, name) -> None:
        self.name = name


class AdressBook(UserDict):  # додамо логіку пошуку за записами
    pass

def add_record(self):
    

class Record:  # відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    pass


class Phone:  # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    def __init__(self, *args) -> None:
        self.args = args
