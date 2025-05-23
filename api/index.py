import csv
import os
import json
from urllib.parse import parse_qs

def handler(request):
    names = parse_qs(request["queryString"]).get("name", [])
    marks = []

    # Load CSV data into a dictionary
    data_path = os.path.join(os.path.dirname(__file__), "students.csv")
    with open(data_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        student_marks = {row["name"]: int(row["marks"]) for row in reader}

    # Find marks for each queried name
    for name in names:
        marks.append(student_marks.get(name, 0))  # de_
