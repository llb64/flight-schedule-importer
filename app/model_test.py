import csv
import os
import model

def test_add_flight():
    # Arrange
    flight_csv_line = "DL,0133,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"
    file_path = "test.csv"
    with open(file_path, "w", newline="") as file:
        csv.writer(file)

    # Act
    model.add_flight(flight_csv_line, file_path)

    # Assert
    with open(file_path, "r") as file:
        first_line = file.readline()
    assert first_line == flight_csv_line + "\n"

    # Clean up
    os.remove(file_path)

def test_delete_flight():
    # Arrange
    flight_csv_lines = [["DL,0133,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"], ["DL,0134,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"], ["DL,0135,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"]]
    file_path = "test.csv"
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(flight_csv_lines)

    # Act
    model.delete_flight(1, file_path)

    # Assert
    with open(file_path, "r") as file:
        lines = file.readlines()
    assert lines == ['"DL,0133,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"\n', '"DL,0135,AMS,2025-11-24 09:20:00Z,2025-11-24 20:20:00Z,11"\n']

    # Clean up
    os.remove(file_path)