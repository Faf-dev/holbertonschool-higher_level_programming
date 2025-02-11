#!/usr/bin/env python3
"""
create a function that transform CSV file data into a dict
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    filename : filename of the CSV file
    """
    data = []

    with open(filename, "r", encoding="utf-8") as csvf:
        csvRead = csv.DictReader(csvf)
        if csvRead is None:
            return False
        for rows in csvRead:
            data.append(rows)

    with open("data.json", "w", encoding="utf-8") as jsonf:
        jsonf.write("[\n\t")
        jsonf.write(",\n\t".join(json.dumps(row) for row in data))
        jsonf.write("\n]")
    return True
