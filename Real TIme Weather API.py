

import os
import csv
import requests
from datetime import datetime

FILENAME = "weather_log.csv"
API_key = "6cd9b8bf9c584866b9b871ed245757d4"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature","Condition"])

def log_weather():
    city = input("Enter City: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "r", newline="", encoding="UTF-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("City and date already exits")
                return


    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("API Error")
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(FILENAME, "a", newline="", encoding="UTF-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city, temp,condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")
    except Exception as e:
        print("Failed to make API call")


def view_logs():
    with open(FILENAME, 'r', encoding="UTF-8") as f:
        reader =  list(csv.reader(f))
        if len(reader) <= 1:
            print("No Enteries")
            return
        for row in reader[1:]:
            print(f"{row[0]:<12} | {row[1]:<15} | {row[2]:<10} | {row[3]}")

def main():
    while True:
        print("Real Time Weather")
        print("1. Add weather log")
        print("2 view Log")

        choice = input("choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()


