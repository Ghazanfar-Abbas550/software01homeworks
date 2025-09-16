import mysql.connector as MyConn
mydb = MyConn.connect(
    host="localhost",
    user="futuretechnologies",
    password="Btno9180?",
    database="flight_game"
)

Area_code = input("Enter Area code: ")
cursor = mydb.cursor()
cursor.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type", (Area_code,))
result = cursor.fetchall()
for row in result:
    print(row[0], ":", row[1])

# Output
# Enter Area code: FI
# closed : 6
# heliport : 15
# large_airport : 1
# medium_airport : 30
# small_airport : 65