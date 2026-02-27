from datetime import datetime

# 1. Создайте словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

# 2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализуйте e-mail адреса
email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлеките логин и домен отправителя
login, domain = email["from"].split('@')

# 5. Создайте сокращённую версию текста
short_body = f"{email["body"][:10]}..."
email["short_body"] = short_body

# 6. Списки доменов
personal_domains_list = ['gmail.com',
                         'list.ru',
                         'yahoo.com',
                         'outlook.com',
                         'hotmail.com',
                         'icloud.com',
                         'yandex.ru',
                         'mail.ru',
                         'list.ru',
                         'bk.ru',
                         'inbox.ru'
                         ]

set_personal_domains_list = set(personal_domains_list)

corporate_domains_list = ['company.ru',
                          'corporation.com',
                          'university.edu',
                          'organization.org',
                          'company.ru',
                          'business.net'
                          ]
set_corporate_domains_list = set(corporate_domains_list)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
common_domains = list(set_personal_domains_list & set_corporate_domains_list)

# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in set_corporate_domains_list

# 9. Соберите «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
                    Тема: {email["subject"]}, дата {email["date"]} 
                    {email["clean_body"]}"""

# 11. Рассчитайте количество страниц печати
text_length = len(email["sent_text"])
pages = (text_length + 499) // 500

# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создайте «маску» e-mail отправителя
email["masked_from"] = f"{login[:2]}***@{domain}"

# 14. Удалите из списка личных доменов значения
set_personal_domains_list.remove("list.ru")
set_personal_domains_list.remove("bk.ru")

print(f"1 task: {email}")
print(f"2 task: {email["date"]}")
print(f"3 task: email[from] = {email["from"]}, email[to] = {email["to"]} ")
print(f"4 task: login = {login}, domain = {domain}")
print(f"5 task: short_body = {short_body}")
print(
    f"6 task: unique_personal_domains_list =  {set_personal_domains_list}, "
    f"unique_corporate_domains_list =  {set_corporate_domains_list}")
print(f"7 task: {common_domains}")
print(f"9 task: {email["clean_body"]}")
print(f"10 task: {email["sent_text"]}")
print(f"11 task: {pages}")
print(f"13 task:{email["masked_from"]}")
