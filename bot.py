from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of the Record class")
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)


class Record:
    def __init__(self, name: str, phones: list) -> None:
        self.name = name
        self.phones = [phone] if phones else []

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        # index = self.phones.index(phone)
        # self.phones[index] = new_phone
        # list(map(lambda phone: self.phones.replace(phone, new_phone), self.phones))
        [new_phone if item == phone else item for item in self.phones]

    def __repr__(self):
        return self.name, self.phones


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

    name = Name("Kim")
    phone = Phone("7386492")
    rec1 = Record(name, phone)

    rec1.add_phone("02384702")
    rec1.add_phone("0238")
    rec1.add_phone("02384")

    rec1.del_phone("1234567890")

    ab1 = AddressBook()
    ab1.add_record(rec1)
    ab1.find_record("0238")
    rec1.edit_phone("0238", "098")
