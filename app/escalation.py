import json
from datetime import datetime
from pathlib import Path


def create_escalation(employee_name, reason):

    escalation = {
        "status": "REQUIRES_HUMAN_INTERVENTION",
        "timestamp": str(datetime.now()),
        "employeeName": employee_name,
        "reason": reason,

        # Human workflow

        "state": "PENDING",
        "selectedEmployeeId": None
    }

    file_name = (
        datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".json"
    )

    path = Path(
        "evidence/escalations"
    ) / file_name

    with open(path, "w") as f:
        json.dump(
            escalation,
            f,
            indent=4
        )

    print(
        f"Escalation saved: {path}"
    )

    return escalation