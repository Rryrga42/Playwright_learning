import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
from pom.form_page import FormPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    fill_form = FormPage(page)


