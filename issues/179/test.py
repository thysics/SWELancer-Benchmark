from playwright.sync_api import sync_playwright, expect
import time

def test():
    with sync_playwright() as p:

        # Step 1: Main Browser Login
        browser = p.chromium.launch(headless=False, args=[
                        "--disable-web-security",
                        "--disable-features=IsolateOrigins,site-per-process"],
                        slow_mo=500)
        
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://dev.new.expensify.com:8082')

        page.get_by_test_id("username").click()
        page.get_by_test_id("username").fill("totherandomuser+511661739843893.6195102@gmail.com")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Join").click()
        page.get_by_label("Manage my team's expenses").click()
        page.get_by_label("-10 employees").click()
        page.get_by_role("button", name="Continue").click()
        page.get_by_label("None of the above").click()
        page.get_by_test_id("BaseOnboardingAccounting").get_by_role("button", name="Continue").click()
        page.get_by_label("My settings").click()
        page.get_by_test_id("InitialSettingsPage").get_by_label("Workspaces").click()
        page.get_by_label("row").click()
        page.get_by_label("Workflows").click()
        page.get_by_label("Connect bank account").click()

        try:
            page.get_by_label("Connect online with Plaid").click()
            expect(page.get_by_text("Validate your account", exact=True)).to_be_visible()
        except:
            raise AssertionError("Connect online with Plaid is not clickable")        


