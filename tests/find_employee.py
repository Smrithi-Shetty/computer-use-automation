from playwright.sync_api import sync_playwright

EMPLOYEE_NAME = "Alice"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Login
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    page.wait_for_load_state("networkidle")

    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")

    page.get_by_role("button", name="Login").click()

    page.wait_for_load_state("networkidle")

    print("Logged In")

    # Open PIM
    page.get_by_role("link", name="PIM").click()

    page.wait_for_load_state("networkidle")

    print("PIM Opened")

    # Search Employee
    page.get_by_role("textbox", name="Type for hints...").first.fill(
        EMPLOYEE_NAME
    )

    page.get_by_role("button", name="Search").click()

    page.wait_for_load_state("networkidle")

    print("Search Complete")

    print("Current URL:", page.url)

    input("Press Enter to close...")

    browser.close()