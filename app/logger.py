import json
from datetime import datetime
from pathlib import Path


def save_replay_log(result):

    log_folder = Path(
        "evidence/replay_logs"
    )

    log_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    log_file = (
        log_folder /
        f"{timestamp}.json"
    )

    with open(log_file, "w") as f:
        json.dump(
            result,
            f,
            indent=4
        )

    print(
        f"Replay log saved: {log_file}"
    )