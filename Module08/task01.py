import mysql.connector as MyConn
mydb = MyConn.connect(
    host="localhost",
    user="futuretechnologies",
    password="Btno9180?",
    database="flight_game"
)


ICAO = input("Enter your ICAO code: ")
cursor = mydb.cursor()
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (ICAO,))
result = cursor.fetchone()
if result == None:
    print("Invalid ICAO code")
else:
    print(result)


# Output
# Enter your ICAO code: EFHK
# ('Helsinki Vantaa Airport', 'Helsinki')