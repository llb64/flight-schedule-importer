import csv

FLIGHTS_PATH = "app/data/flights.csv"
USERS_PATH = "app/data/users.csv"

def load_users():
    with open(USERS_PATH, newline="") as users:
        return list(csv.DictReader(users))

def load_flight_data():
    with open(FLIGHTS_PATH, newline="") as flights:
        next(flights)
        return list(csv.reader(flights))

def add_flight(flight_csv):
    with open(FLIGHTS_PATH, 'a', newline="") as flights:
        flights.write(flight_csv + "\n")

def delete_flight(index):
    with open(FLIGHTS_PATH, newline="") as flights:
        rows = list(csv.reader(flights))
    
    del rows[index]

    with open(FLIGHTS_PATH, "w", newline="") as flights:
        writer = csv.writer(flights)
        writer.writerows(rows)
