import requests

# Fetch a random Chuck Norris joke
response = requests.get("https://api.chucknorris.io/jokes/random")

# Convert the response to JSON format
data = response.json()

# Print only the joke text
print(data["value"])