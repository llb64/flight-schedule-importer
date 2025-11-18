import csv

FLIGHTS_PATH = "app/data/flights.csv"
USERS_PATH = "app/data/users.csv"

def load_flight_data():
    with open(FLIGHTS_PATH, newline="") as flights:
        next(flights)
        return list(csv.reader(flights))

def load_users():
    with open(USERS_PATH, newline="") as users:
        return list(csv.DictReader(users))
