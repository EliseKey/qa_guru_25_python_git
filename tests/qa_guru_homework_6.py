## Часть A. Функции
from datetime import datetime


# Нормализация email адресов
def normalize_addresses(value: str) -> str:
    return value.lower().strip()


# Сокращенная версия тела письма
def add_short_body(email: dict) -> dict:
    email["short_body"] = f"{email["body"][:10]}..."
    return email


# Очистка текста письма
def clean_body_text(body: str) -> str:
    return body.replace("\t", " ").replace("\n", " ")


# Формирование итогового текста письма
def build_sent_text(email: dict) -> str:
    return f"""Кому: {email["recipient"]}, от {email["sender"]}
                    Тема: {email["subject"]}, дата {email["date"]} {email["body"]}"""


# Проверка пустоты темы и тела
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    return not bool(subject.strip()), not bool(body.strip())


# Маска email отправителя
def mask_sender_email(login: str, domain: str) -> str:
    return f"{login[:2]}***@{domain}"


# Проверка корректности email адресов
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_email_list = []
    for email in email_list:
        if '@' in email and email.lower().strip().endswith(('.com', '.ru', '.net')):
            correct_email_list.append(email)
    return correct_email_list


# Список emails для проверки работы функции
test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]


# Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    return {'sender': sender, 'recipient': recipient, 'subject': subject, 'body': body}


# Добавление даты отправки
def add_send_date(email: dict) -> dict:
    email["date"] = datetime.now().strftime("%Y-%m-%d")
    return email


# Получение логина и домена
def extract_login_domain(address: str) -> tuple[str, str]:
    login, domain = address.split('@')
    return login, domain


## Часть B. Отправка письма


# Создать функцию отправки письма с базовой валидацией адресов
def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    if not recipient_list:
        print("Ошибка: список получателей пуст")
        return []

    correct_recipient = get_correct_email(test_emails)
    if not correct_recipient:
        print(f"Ошибка: email отправителя {sender} некорректен")
        return []

    subject_empty, body_empty = check_empty_fields(subject, message)
    if subject_empty or body_empty:
        print("Ошибка: тема или тело письма пустые")
        return []

    filtered_recipients = []
    for item in recipient_list:
        if item != sender:
            filtered_recipients.append(item)
        else:
            print(f"Исключена отправка самому себе: {item}")

    recipient_list = filtered_recipients
    cleaned_subject = clean_body_text(subject)
    cleaned_message = clean_body_text(message)

    normalized_recipient_list = [normalize_addresses(recipient)
                                 for recipient in filtered_recipients]

    normalized_sender = normalize_addresses(sender)

    emails = []

    for recipient in normalized_sender:
        email = create_email(
            normalized_sender, recipient, cleaned_subject, cleaned_message
        )

        add_send_date(email)
        login, domain = extract_login_domain(normalized_sender)
        mask_sender_email(login, domain)
        add_short_body(email)
        email["sent_text"] = build_sent_text(email)
        emails.append(email)

        return emails
