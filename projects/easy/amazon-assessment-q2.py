#!/bin/python3

import json
import re
import sys


def evaluate_deployments(deployments):
    success_count = 0
    fail_count = 0
    error_count = 0

    deployment_id_pattern = r"^d-[a-z0-9]{10}$"

    for deployment_str in deployments:
        try:
            deployment = json.loads(deployment_str)

            deployment_id = deployment.get("deployment_id")
            status = deployment.get("status")

            if not deployment_id or not re.match(deployment_id_pattern, deployment_id):
                error_count += 1
                continue

            if status == "Success":
                success_count += 1
            elif status == "Fail":
                fail_count += 1
            else:
                error_count += 1

        except (json.JSONDecodeError, TypeError, ValueError):
            error_count += 1

    return [success_count, fail_count, error_count]


if __name__ == '__main__':
    n = int(input().strip())
    deployments = []

    for _ in range(n):
        deployments.append(input().strip())

    result = evaluate_deployments(deployments)

    for count in result:
        print(count)