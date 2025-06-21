#!/usr/bin/python3
"""Convert CSV file to JSON format and save as data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV data to JSON and saves it to 'data.json'.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if conversion was successful, False if an error occurred.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
