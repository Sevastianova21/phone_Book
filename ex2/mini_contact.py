class Contact:
    def __init__(self, name: str, email: str, phone_number: str):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f'Имя: {self.name}    Email: {self.email}    Номер телефона: {self.phone_number}\n'
