def send_email(recipient, *, sender="university.help@gmail.com"):
    valid_fixes = [".com", ".ru", ".net"]
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе! Отправитель: {sender}, Получатель: {recipient}")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    if not all(char in sender for char in '@.') or sender[-4:] not in valid_fixes:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('vlad@gmail.com')
send_email('urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('urban.teacher@mail.ru', sender='urban.teacher@mail.ru')