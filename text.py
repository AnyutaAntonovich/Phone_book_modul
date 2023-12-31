main_menu = ['Главное меню:',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

user_choice = 'Выберите пункт меню: '
user_choice_error = f'Ошибка ввода! Выберите пункт меню от 1 до {len(main_menu) - 1}'

open_successful = 'Телефонная книга успешно загружена!'
save_successful = 'Телефонная книга успешно сохранена!'

empty_phone_book_error = 'Телефонная книга пуста или не загружена!'

input_new_contact = ['Введите фамилию и имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комментарий: ']

input_edit_contact = ['Введите новые фамилию и имя контакта или ENTER, чтобы оставить без изменений: ',
                     'Введите новый номер контакта или ENTER, чтобы оставить без изменений: ',
                     'Введите новый комментарий или ENTER, чтобы оставить без изменений: ']

contact_action = ['сохранен', 'изменен', 'удален']

input_search_word = 'Введите слово для поиска: '
input_search_word_edit = 'Введите слово для поиска контакта, который хотите изменить: '
input_search_word_delete = 'Введите слово для поиска контакта, который хотите удалить: '

input_id_edit = 'Введите ID изменяемого контакта: '
input_id_delete = 'Введите ID удаляемого контакта: '

good_bye = 'Всего хорошего! До новых встреч!'


def contact_info(name: str, option: int) -> str:
    return f'Контакт {name} успешно {contact_action[option]}!'


def search_word_error(word: str) -> str:
    return f'Контакты, содержащие "{word}" не найдены!'
