

import json
from datetime import datetime
import os
import gspread
from google import genai
from google.oauth2.service_account import Credentials

# =========================
# CONFIGURATION
# =========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SERVICE_ACCOUNT_FILE = "service_account.json"
SPREADSHEET_NAME = "My Workouts"


# =========================
# GEMINI FUNCTIONS
# =========================

def configure_gemini():
    """Create and return Gemini client."""
    return genai.Client(api_key=GEMINI_API_KEY)


def get_exercise_data(client, exercise_text):
    """Send exercise text to Gemini and return parsed JSON."""

    prompt = f"""
    Convert the workout description into JSON.

    Return ONLY valid JSON.

    Format:

    [
        {{
            "exercise": "",
            "duration": 0,
            "calories": 0
        }}
    ]

    Rules:
    - Duration must be in minutes.
    - Calories must be estimated.
    - Return valid JSON only.

    Workout:
    {exercise_text}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_text)


# =========================
# GOOGLE SHEETS FUNCTIONS
# =========================

def connect_to_sheet():
    """Connect to Google Sheet."""

    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    sheet = client.open(
        SPREADSHEET_NAME
    ).sheet1

    return sheet


def save_workout(sheet, workout_data):
    """Save workout data to Google Sheet."""

    now = datetime.now()

    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%I:%M %p")

    for exercise in workout_data:
        row = [
            current_date,
            current_time,
            exercise["exercise"].title(),
            exercise["duration"],
            exercise["calories"]
        ]

        sheet.append_row(row)

        print(
            f"✅ Saved: "
            f"{exercise['exercise']} | "
            f"{exercise['duration']} min | "
            f"{exercise['calories']} cal"
        )


# =========================
# MAIN PROGRAM
# =========================

def main():
    print("\n🏃 Workout Tracker\n")

    exercise_text = input(
        "Tell me which exercises you did today:\n"
    )

    gemini_client = configure_gemini()

    workout_data = get_exercise_data(
        gemini_client,
        exercise_text
    )

    print("\nDetected Workouts:")
    print(workout_data)

    sheet = connect_to_sheet()

    save_workout(
        sheet,
        workout_data
    )

    print("\n✅ Workout successfully saved!")


if __name__ == "__main__":
    main()
