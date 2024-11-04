from playwright.sync_api import expect

class HomePage:

    def __init__(self,page):
        self.elements_header = page.locator("text=Elements")

        self.forms_header = page.locator("text=Forms")

        self.alerts_frame_and_windows = page.locator("text=Alerts, Frame & Windows")

        self.widgets = page.locator("text=Widgets")

        self.interactions = page.locator("text=Interactions")

        self.book_store_applications = page.locator("text=Book Store Application")

    def click_elements(self):
        try:
            expect(self.elements_header).to_be_visible()
            self.elements_header.click()
        except Exception as e:
            print(f"Failed to click on Elements: {e}")

    def click_forms(self):
        try:
            expect(self.forms_header).to_be_visible()
            self.forms_header.click()
        except Exception as e:
            print(f"Failed to click on Forms: {e}")

    def click_alerts_frame_and_windows(self):
        try:
            expect(self.alerts_frame_and_windows).to_be_visible()
            self.alerts_frame_and_windows.click()
        except Exception as e:
            print(f"Failed to click on Alerts_frame_and_windows: {e}")

    def click_widgets(self):
        try:
            expect(self.widgets).to_be_visible()
            self.widgets.click()
        except Exception as e:
            print(f"Failed to click on Widgets: {e}")

    def click_interactions(self):
        try:
            expect(self.interactions).to_be_visible()
            self.interactions.click()
        except Exception as e:
            print(f"Failed to click on Interactions: {e}")

    def click_book_store_applications(self):
        try:
            expect(self.book_store_applications).to_be_visible()
            self.book_store_applications.click()
        except Exception as e:
            print(f"Failed to click on Book_store_applications: {e}")
