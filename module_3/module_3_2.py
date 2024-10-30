def send_email(message, recipient, sender="university.help@gmail.com"):  # ф-ия с 2-мя обычными арг-ами и 1 именованным
    a = ('.com', '.ru', '.net')  # создаем кортеж для упрощения чтения следующего условия
    if ('@' not in recipient or '@' not in sender) or (not recipient.endswith(a) or not sender.endswith(a)):
        # проверяем отсутствие @ в двух аргументах функции
        # или отсутствие какого-либо элемента из кортежа "а" в конце двух аргументов функции
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)  # if True -> print
    elif sender == recipient:  # проверяем равенство двух аргументов функции
        print('Нельзя отправить письмо самому себе!')  # if True -> print
    elif sender == "university.help@gmail.com": # проверяем не изменен ли именованный аргумент функции
        print('Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient + '.') # if True -> print
    else: # если предыдущие условия не сработали выводим следующих текст:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient + '.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
