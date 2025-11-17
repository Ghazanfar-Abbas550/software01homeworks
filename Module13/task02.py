from flask import Flask, Response
import json

app = Flask(__name__)

# Airport database (ICAO: [Name, Location])
airports = {
    "EFHK": ["Helsinki-Vantaa Airport", "Helsinki"],
    "EGLL": ["London Heathrow Airport", "London"],
    "KJFK": ["John F. Kennedy International Airport", "New York"],
    "OMDB": ["Dubai International Airport", "Dubai"],
    # Add more ICAO codes here if needed
}

@app.route('/airport/<icao>')
def airport_info(icao):
    icao = icao.upper()  # Normalize input (e.g. efhk → EFHK)
    if icao in airports:
        name, location = airports[icao]
        response = {
            "ICAO": icao,
            "Name": name,
            "Location": location,
            "status": 200
        }
        return response
    else:
        response = {
            "message": f"ICAO code '{icao}' not found",
            "status": 404
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=404, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=5000)