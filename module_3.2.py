def check_email(email):
    if (
            "@" in email and
            email.endswith((".com", ".ru", ".net"))):
        result = True
    else:
        result = False
    return result


def send_email(message, recipient, sender="urban@gmail.com"):
    if not (check_email(sender) and check_email(recipient)):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправлять письмо самому себе')
    elif sender == "urban@gmail.com":
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! письмо отправлено с адреса', sender, 'на адрес', recipient)



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# output = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
# output = 'Нельзя отправлять письмо самому себе'
# output = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
# output = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! письмо отправлено с адреса {sender} на адрес {recipient}'
