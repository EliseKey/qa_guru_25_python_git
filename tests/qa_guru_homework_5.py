import os
import time

from selene import browser, be, have


def test_submit_form():
    # Открытие страницы
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('.text-center').should(have.text('Practice Form'))

    # Заполнение контактной информации
    browser.element('#firstName').type('Test firstName')
    browser.element('#lastName').type('Test lastName')
    browser.element('#userEmail').type('user_email@test.com')
    browser.element('#genterWrapper').element('[value="Female"]').click()
    browser.element('#userNumber').type('8988112234')

    # Заполнение дополнительной информации
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1999"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__day--023').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#hobbiesWrapper').element('[value="2"]').click()

    # Загрузка файла
    image_path = os.path.join(os.path.dirname(__file__), 'test_data', 'test_pic.jpg')
    browser.element('#uploadPicture').send_keys(image_path)

    # Заполнение адреса
    browser.element('#currentAddress').type('Disneyland Resort, Anaheim, California, United States')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    # Отправка формы
    browser.element('#submit').click()

    # Проверяем корректность данных после отправки формы
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-content').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Test firstName Test lastName',
            'Student Email user_email@test.com',
            'Gender Female',
            'Mobile 8988112234',
            'Date of Birth 23 January,1999',
            'Subjects Maths',
            'Hobbies Reading',
            'Picture test_pic.jpg',
            'Address Disneyland Resort, Anaheim, California, United States',
            'State and City NCR Gurgaon'
        )
    )
