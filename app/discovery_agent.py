import json

from replay_engine import execute_capability

def discover_capability(goal):

    goal = goal.strip()

    # Just employee name

    if len(goal.split()) == 1:

        return {
            "capability": "FindEmployee",
            "employeeName": goal.title()
        }

    # Natural language

    if "find employee" in goal.lower():

        employee_name = (
            goal.lower()
            .replace(
                "find employee",
                ""
            )
            .strip()
            .title()
        )

        return {
            "capability": "FindEmployee",
            "employeeName": employee_name
        }

    return {
        "status": "UNSUPPORTED_GOAL"
    }


if __name__ == "__main__":

    goal = input(
        "Enter Goal: "
    )

    discovery_result = discover_capability(
        goal
    )

    print(
        json.dumps(
            discovery_result,
            indent=4
        )
    )

    # Execute capability

    if discovery_result.get(
        "capability"
    ) == "FindEmployee":

        replay_result = execute_capability(
            discovery_result[
                "employeeName"
            ]
        )

        print("\nReplay Result:\n")

        print(
            json.dumps(
                replay_result,
                indent=4
            )
        )