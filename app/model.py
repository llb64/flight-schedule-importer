import csv

FLIGHTS_PATH = "app/data/flights.csv"
USERS_PATH = "app/data/users.csv"

def load_users():
    with open(USERS_PATH, newline="") as users:
        return list(csv.DictReader(users))
    
def read_csv_file(csv_file_path):
    with open(csv_file_path, newline="") as lines:
        next(lines)
        return list(csv.reader(lines))

def load_flight_data():
    return read_csv_file(FLIGHTS_PATH)
    
def load_flight_schedule_file(flight_schedule_file_path):
    return read_csv_file(flight_schedule_file_path)

def add_flight(flight_csv, csv_path = FLIGHTS_PATH):
    with open(csv_path, 'a', newline="") as flights:
        flights.write(flight_csv + "\n")

def delete_flight(index, csv_path = FLIGHTS_PATH):
    with open(csv_path, newline="") as flights:
        rows = list(csv.reader(flights))
    
    del rows[index]

    with open(csv_path, "w", newline="") as flights:
        writer = csv.writer(flights)
        writer.writerows(rows)
