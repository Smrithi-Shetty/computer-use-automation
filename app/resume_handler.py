import json
from pathlib import Path


def get_latest_escalation():

    escalation_folder = Path(
        "evidence/escalations"
    )

    files = list(
        escalation_folder.glob("*.json")
    )

    if not files:
        return None

    latest_file = max(
        files,
        key=lambda f: f.stat().st_mtime
    )

    return latest_file


def resume_execution():

    latest_file = get_latest_escalation()

    if latest_file is None:

        return {
            "status": "NO_ESCALATIONS_FOUND"
        }

    with open(latest_file, "r") as f:

        escalation = json.load(f)

    if escalation["state"] != "APPROVED":

        return {
            "status": "WAITING_FOR_APPROVAL",
            "employeeName":
                escalation["employeeName"],
            "sourceEscalation":
                latest_file.name
        }

    return {
        "status": "RESUMED",
        "employeeId":
            escalation["selectedEmployeeId"],
        "employeeName":
            escalation["employeeName"],
        "sourceEscalation":
            latest_file.name,
        "message":
            f"Human selected employee "
            f"{escalation['selectedEmployeeId']}"
    }


if __name__ == "__main__":

    result = resume_execution()

    print(
        json.dumps(
            result,
            indent=4
        )
    )