import requests
# Project: weather-app
required_data = ["pressure", "humidity", "description", "temp", "feels_like", "speed"]

def checkWeather():
    location = input("Location: ")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": "04e7a955215e9915959051a130de2b54",
        "units": "metric"
    }

    response = requests.get(url, params=params)
    if response.status_code == 500:
        return print("Location not found!")
    data = response.json()
    print("-------------------------")
    for key, value in data.items():
        if key == 'weather':
            for k, v in value[0].items():
                if k in required_data:
                    print(f"{k}: {v}")
        elif key == 'main':
            for k, v in value.items():
                if k in required_data:
                    print(f"{k}: {v}")
        elif key == 'wind':
            for k, v in value.items():
                if k in required_data:
                    print(f"{k}: {v}")
    print("-------------------------")

print("|---------Weather-App---------|")
while True:
    command = input("Command: ")
    if command == "check weather":
        checkWeather()
    elif command == "exit":
        print("|---------App-Closed----------|")
        break
    else:
        print("The syntax of the command is incorrect! (use 'exit')")
