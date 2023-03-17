import mini_contact


def show_contact():
    data = open('phone.txt', 'r', encoding='UTF-8')
    i = 1
    for line in data:
        print(i, line)
        i = i + 1
    data.close()


class ContactBook:
    contacts = []

    def __init__(self):
        with open('phone.txt', 'r', encoding='UTF-8') as file:
            all_contacts = file.readlines()
            for i in range(len(all_contacts)):
                contact_str = all_contacts[i].split('   ')
                self.contacts.append(
                    mini_contact.Contact((contact_str[0][5:]), (contact_str[1][8:]), contact_str[2][17:(-2)]))

    def save_contact(self):
        data = open('phone.txt', 'w', encoding='UTF-8')
        for i in range(len(self.contacts)):
            data.write(str(self.contacts[i]))
        data.close()

    def add_contact(self):
        self.contacts.append(
            mini_contact.Contact(input('Введите имя\n'), input('Введите Email\n'), input('Введите номер телефона\n')))

    def rewrite_contact(self):
        string_number = int(input('Введите порядковый номер контакта, который хотите изменить\n'))
        match int(input('Изменить   1. Имя    2.Email     3. номер телефона\n')):
            case 1:
                self.contacts[string_number - 1].name = input('Новое имя \n')
            case 2:
                self.contacts[string_number - 1].email = input('Новый Email \n')
            case 3:
                self.contacts[string_number - 1].phone_number = input('Новый номер \n')

    def find_contact(self):
        find = input(' Введите имя, номер или Email \n')
        for i in range(len(self.contacts)):
            if self.contacts[i].name == find or self.contacts[i].email == find or self.contacts[i].phone_number == find:
                print(i + 1, self.contacts[i])

    def delete_contact(self):
        number = int(input('Введите номер строки контакта для удаления\n'))
        self.contacts.pop(number - 1)
