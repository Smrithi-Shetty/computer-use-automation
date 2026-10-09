from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.wait_for_timeout(3000)

    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")

    page.get_by_role("button", name="Login").click()

    page.wait_for_timeout(5000)

    print("Title:", page.title())
    print("URL:", page.url)

    input("Press Enter to close browser...")

    browser.close()