from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(
        self,
        value,
    ) -> None:
        super().__init__(value)


class Record:
    def __init__(self, name: str, phones=None) -> None:
        self.name = name
        self.phones = [phone] if phones else []

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def del_record(self, phone):
        self.phones.remove(phone)

    def edit_record(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class AddressBook(UserDict):
    def find_record(self, value):
        return self.data.get(value)

    def add_record(self, record):
        if not isinstance(rec, Record):
            raise ValueError("Record must be an instance of the Record class")
        self.data[record.name.value] = record


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
