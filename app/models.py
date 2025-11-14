import csv

FLIGHTS_PATH = "app/data/flights.csv"

def load_flight_data():
    with open(FLIGHTS_PATH, newline="") as flightdata:
        next(flightdata)
        return list(csv.reader(flightdata))