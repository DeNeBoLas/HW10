from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        # self.name = name

    def add_name(self):
        return self.name


class AddressBook(UserDict):
    def find_record(self, value):
        return self.data.get(value)

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None) -> None:
        self.name = name
        self.phones = [phone] if phone else []


class Phone(Field):
    def __init__(self, value, number=None) -> None:
        super().__init__(value)
        self.number = number


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"
    print("All Ok)")
