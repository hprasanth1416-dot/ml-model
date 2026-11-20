import os

import requests


BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

student_data = {
    "study_hours": 5.0,
    "attendance": 80.0,
    "previous_marks": 75.0,
}

response = requests.post(
    f"{BASE_URL}/predict",
    json=student_data,
    timeout=10,
)

print("STATUS CODE:", response.status_code)
print("PREDICTION RESULT:", response.json())

response.raise_for_status()
