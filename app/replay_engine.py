import json
from datetime import datetime
from logger import save_replay_log
from escalation import create_escalation

from playwright.sync_api import sync_playwright


def load_artifact(path):
    with open(path, "r") as f:
        return json.load(f)


def execute_capability(employee_name):

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)

            page = browser.new_page()

            # Login

            page.goto(
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            )

            page.wait_for_load_state("networkidle")

            page.locator(
                'input[name="username"]'
            ).fill("Admin")

            page.locator(
                'input[name="password"]'
            ).fill("admin123")

            page.get_by_role(
                "button",
                name="Login"
            ).click()

            page.wait_for_load_state("networkidle")

            # Open PIM

            page.get_by_role(
                "link",
                name="PIM"
            ).click()

            page.wait_for_load_state("networkidle")

            # Search Employee

            page.get_by_role(
                "textbox",
                name="Type for hints..."
            ).first.fill(employee_name)

            page.get_by_role(
                "button",
                name="Search"
            ).click()

            page.wait_for_timeout(3000)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            page.screenshot(
                path=f"evidence/screenshots/{employee_name}_{timestamp}.png",
                full_page=True
            )

            # Results

            rows = page.locator(
                ".oxd-table-body .oxd-table-row"
            )

            row_count = rows.count()

            print(f"Rows Found: {row_count}")

            # Too many matches, needs human review
            if row_count > 5:

                browser.close()

                return create_escalation(
                    employee_name,
                    f"{row_count} matching employees found. Human review required."
                )

            # ---------------------------------
            # No Employee Found
            # ---------------------------------

            if row_count == 0:

                browser.close()

                return {
                    "status": "EMPLOYEE_NOT_FOUND",
                    "capability": "FindEmployee",
                    "executionTime": str(datetime.now()),
                    "input": {
                        "employeeName": employee_name
                    },
                    "message": (
                        f"No employee found matching "
                        f"'{employee_name}'"
                    )
                }

            # ---------------------------------
            # One or More Employees Found
            # ---------------------------------

            matches = []

            for i in range(row_count):

                row = rows.nth(i)

                matches.append(
                    {
                        "employeeId": row.locator(
                            ".oxd-table-cell"
                        ).nth(1).inner_text(),

                        "firstName": row.locator(
                            ".oxd-table-cell"
                        ).nth(2).inner_text(),

                        "lastName": row.locator(
                            ".oxd-table-cell"
                        ).nth(3).inner_text()
                    }
                )

            browser.close()

            return {
                "status": "SUCCESS",
                "capability": "FindEmployee",
                "executionTime": str(datetime.now()),
                "matchCount": row_count,
                "input": {
                    "employeeName": employee_name
                },
                "matches": matches
            }

    except Exception as ex:

        return {
            "status": "FAILURE",
            "capability": "FindEmployee",
            "executionTime": str(datetime.now()),
            "input": {
                "employeeName": employee_name
            },
            "error": str(ex)
        }


if __name__ == "__main__":

    artifact = load_artifact(
        "artifacts/find_employee_v1.json"
    )

    employee_name = input(
        "Enter Employee Name: "
    )

    print(
        f"Loaded Capability: "
        f"{artifact['capability']['name']}"
    )

    result = execute_capability(
        employee_name
    )

    save_replay_log(result)

    print(
        json.dumps(
            result,
            indent=4
        )
    )