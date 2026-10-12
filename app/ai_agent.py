import json

from discovery_agent import discover_capability
from replay_engine import execute_capability


def process_goal(goal):

    discovery_result = discover_capability(
        goal
    )

    if (
        discovery_result.get(
            "capability"
        )
        == "FindEmployee"
    ):

        return execute_capability(
            discovery_result[
                "employeeName"
            ]
        )

    return {
        "status":
            "UNSUPPORTED_GOAL"
    }


if __name__ == "__main__":

    goal = input(
        "Enter Goal: "
    )

    result = process_goal(
        goal
    )

    print(
        json.dumps(
            result,
            indent=4
        )
    )