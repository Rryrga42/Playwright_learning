import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.locator("div:nth-child(4) > div > .avatar > svg").click()
    page.get_by_text("Accordian").click()
    page.get_by_text("Auto Complete").click()
    page.locator(".auto-complete__value-container").first.click()
    page.locator("#autoCompleteMultipleInput").fill("dfdfdf")
    page.locator("#autoCompleteSingleContainer > .auto-complete__control > .auto-complete__value-container").click()
    page.locator("#autoCompleteSingleInput").fill("dfdfdfdfdf")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
