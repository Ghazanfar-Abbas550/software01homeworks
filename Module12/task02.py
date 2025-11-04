import requests

city = input("Enter the name of a municipality: ")

api_key = "YOUR_API_KEY"  # Replace with your actual key

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

# Check if the API request was successful
if response.status_code == 200 and "weather" in data:
    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    print(f"Weather in {city}: {description}, {temp_celsius:.1f} °C")
else:
    # Print the error message from API if available
    print("Error fetching data:")
    print(data.get("message", "Unknown error"))