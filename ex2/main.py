import ContactBook
import menu

menu.print_menu()
what_to_do = 0
while what_to_do < 8:
    what_to_do = menu.get_number()
    match what_to_do:
        case 1:
            contacts = ContactBook.ContactBook()
        case 2:
            contacts.save_contact()
        case 3:
            ContactBook.show_contact()
        case 4:
            contacts.add_contact()
        case 5:
            contacts.rewrite_contact()
        case 6:
            contacts.find_contact()
        case 7:
            contacts.delete_contact()
        case 8:
            print('завершение работы со справочником')
