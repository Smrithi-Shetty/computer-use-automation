import json


def load_artifact(path):
    with open(path, "r") as f:
        return json.load(f)


def execute_capability(employee_name):
    print(f"Executing FindEmployee for {employee_name}")


if __name__ == "__main__":

    artifact = load_artifact(
        "artifacts/find_employee_v1.json"
    )

    print(
        f"Loaded Capability: "
        f"{artifact['capability']['name']}"
    )

    execute_capability("Alice")