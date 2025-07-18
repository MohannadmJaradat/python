#!/bin/python3

import sys


def ordered_configuration(configuration):
    if not configuration or not configuration.strip():
        return ["Invalid configuration"]

    entries = configuration.strip().split('|')

    index_set = set()
    value_set = set()
    config_map = {}

    for entry in entries:
        if len(entry) != 14:
            return ["Invalid configuration"]

        ordinal_str = entry[:4]
        config_value = entry[4:]

        if not ordinal_str.isdigit() or ordinal_str == "0000":
            return ["Invalid configuration"]

        if len(config_value) != 10 or not config_value.isalnum():
            return ["Invalid configuration"]

        if ordinal_str in index_set or config_value in value_set:
            return ["Invalid configuration"]

        index_set.add(ordinal_str)
        value_set.add(config_value)
        config_map[int(ordinal_str)] = config_value

    sorted_indices = sorted(config_map.keys())
    if sorted_indices != list(range(1, len(entries) + 1)):
        return ["Invalid configuration"]

    return [config_map[i] for i in sorted_indices]


if __name__ == '__main__':
    configuration = input().strip()
    result = ordered_configuration(configuration)
    for line in result:
        print(line)