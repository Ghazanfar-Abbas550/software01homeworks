import mysql.connector as MyConn
mydb = MyConn.connect(
    host="localhost",
    user="futuretechnologies",
    password="Btno9180?",
    database="flight_game"
)

ICAO1 = input("Enter ICAO code #1: ")
ICAO2 = input("Enter ICAO code #2: ")
cursor = mydb.cursor()
cursor.execute("SELECT latitude_deg, longitude_deg from airport WHERE ident = %s", (ICAO1,))
result1 = cursor.fetchone()
cursor.execute("SELECT latitude_deg, longitude_deg from airport WHERE ident = %s", (ICAO2,))
result2 = cursor.fetchone()
from geopy.distance import distance

dist_km = distance(result1, result2).km
print(f"The distance between {ICAO1} and {ICAO2} is {dist_km:.2f} km")
