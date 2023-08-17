import datetime

class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if self.value is not None and not isinstance(self.value, str):
            raise ValueError("Phone number must be a string")
        if self.value is not None and not self.value.isdigit():
            raise ValueError("Phone number can only contain digits")

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value
        self.validate_phone()


class Birthday(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate_birthday()

    def validate_birthday(self):
        if self.value is not None and not isinstance(self.value, datetime.date):
            raise ValueError("Birthday must be a datetime.date object")

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value
        self.validate_birthday()

    def days_to_birthday(self):
        if self.value is None:
            return None

        today = datetime.date.today()
        next_birthday = datetime.date(today.year, self.value.month, self.value.day)
        
        if next_birthday < today:
            next_birthday = datetime.date(today.year + 1, self.value.month, self.value.day)
        
        days_left = (next_birthday - today).days
        return days_left


class Record:
    def __init__(self, phone=None, birthday=None):
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        return self.birthday.days_to_birthday()


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, content_parts):
        for i in range(0, len(self.records), content_parts):
            yield self.records[i:i + content_parts]


if __name__ == "__main__":

    address_book = AddressBook()

    record_1 = Record(phone="0935864755", birthday=datetime.date(1994, 1, 22))
    record_2 = Record(phone="0963928493", birthday=datetime.date(1995, 8, 10))

    address_book.add_record(record_1)
    address_book.add_record(record_2)

    content_parts = 2
    for part in address_book.iterator(content_parts):
        for record in part:
            print("Phone:", record.phone.value)
            if record.birthday.value:
                print("Days to birthday:", record.days_to_birthday())
        