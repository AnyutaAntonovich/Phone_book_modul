phone_book = {}
path = 'phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phone_book[i] = contact


def save_file():
    contacts = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        contacts.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(contacts))



def new_id():
    return max(phone_book) + 1


def new_contact(contact: list[str]):
    phone_book[new_id()] = contact


def search(word: str) -> dict[int, list[str]]:
    result = {}
    for u_id, contact in phone_book.items():
        if word.lower() in ' '.join(contact).lower():
            result[u_id] = contact
    return result


def edit(u_id: int, contact: list[str]) -> str:
    original_contact = phone_book.get(u_id)
    for i in range(len(contact)):
        contact[i] = contact[i] if contact[i] else original_contact[i]
    phone_book[u_id] = contact
    return contact[0]


def delete(u_id: int) -> str:
    return phone_book.pop(u_id)[0]
