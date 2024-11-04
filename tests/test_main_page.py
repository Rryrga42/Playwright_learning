import pytest
from playwright.sync_api import expect
from pom.home_page_elements import HomePage

@pytest.mark.regression
def test_elements_header_visible(page_fixture, base_url):
     # Переходимо на базовий URL (головну сторінку сайту)
    page_fixture.goto(base_url)

     # Створюємо об'єкт HomePage для взаємодії зі сторінкою
    home_page = HomePage(page_fixture)

    expect(home_page.elements_header).to_be_visible()

@pytest.mark.regression
def test_click_elements_section(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_elements()
    expect(page_fixture).to_have_url(f"{base_url}elements")

# Тест на перевірку видимості заголовку розділу Forms
def test_book_store_applications_visible(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_book_store_applications()
    expect(page_fixture).to_have_url(f"{base_url}books")

# Тест на клік по розділу Forms та перевірку переходу
def test_click_forms_section(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_forms()
    expect(page_fixture).to_have_url(f"{base_url}forms")

# Тест на перевірку видимості заголовку Alerts, Frame & Windows
def test_alerts_frame_and_windows_header_visible(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    expect(home_page.alerts_frame_and_windows).to_be_visible()

# Тест на клік по розділу Alerts, Frame & Windows та перевірку переходу
def test_click_alerts_frame_and_windows_section(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_alerts_frame_and_windows()
    expect(page_fixture).to_have_url(f"{base_url}alertsWindows")

# Тест на перевірку видимості заголовку Widgets
def test_widgets_header_visible(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    expect(home_page.widgets).to_be_visible()

# Тест на клік по розділу Widgets та перевірку переходу
def test_click_widgets_section(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_widgets()
    expect(page_fixture).to_have_url(f"{base_url}widgets")
@pytest.mark.smoke
def test_interactions_visible(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_interactions()
    print("Current URL:", page_fixture.url)  # Додано для відладки
    expect(page_fixture).to_have_url(f"{base_url}interaction")

@pytest.mark.smoke
def test_book_store_applications_visible(page_fixture, base_url):
    page_fixture.goto(base_url)
    home_page = HomePage(page_fixture)
    home_page.click_book_store_applications()
    expect(page_fixture).to_have_url(f"{base_url}books")
