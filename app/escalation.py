import json
from datetime import datetime
from pathlib import Path


def create_escalation(employee_name, reason):

    escalation = {
        "status": "REQUIRES_HUMAN_INTERVENTION",
        "timestamp": str(datetime.now()),
        "employeeName": employee_name,
        "reason": reason
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

    return escalation