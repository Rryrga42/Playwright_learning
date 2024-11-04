import pytest
from playwright.sync_api import expect
from pom.form_page import FormPage

def test_open_page(page_fixture, base_url, endpoint):
    url = f"{base_url}{endpoint}"
    if endpoint == "automation-practice-form":
        page_fixture.goto(url)

        # Створюємо екземпляр FormPage
        form_page = FormPage(page_fixture)

        # Перевірка, що URL правильний
        assert page_fixture.url == url

        # Приклад перевірки видимості елемента
        expect(form_page.first_name_input).to_be_visible()
        print(f"Successfully opened URL: {url}")
