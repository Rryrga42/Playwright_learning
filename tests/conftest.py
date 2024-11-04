import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def gender_options():
    return ["Male", "Female", "Other"]

@pytest.fixture
def hobbies_options():
    return ["Sports", "Reading", "Music"]

@pytest.fixture
def states():
    return ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]

@pytest.fixture
def cities():
    return {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }

@pytest.fixture(scope="function")
def page_fixture():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Відкриття браузера в візуальному режимі (headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()

    # Фікстура з базовим URL
@pytest.fixture
def base_url():
    return "https://demoqa.com/"

# Фікстура для різних кінцевих частин URL
@pytest.fixture(params=[
    "",  # Головна сторінка
    "automation-practice-form",  # Сторінка з формою
    "browser-windows",  # Приклад іншої сторінки
    "alerts",  # Сторінка для тестування алертів
    "frames", #Frames page
    "nestedframes", #Nested frames page
    "modal-dialogs" #madal dialogs page
])
def endpoint(request):
    return request.param
