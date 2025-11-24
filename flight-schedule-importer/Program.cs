using NPOI.HSSF.UserModel;
using NPOI.XSSF.UserModel;
using NPOI.SS.UserModel;
using FlightScheduleImporter.Enums;
using FlightScheduleImporter.Extensions;
using System.Globalization;

const string FilePath = "flight-schedule-importer/import_file.xls";
const int StartRowIndex = 5;
const string Carrier = "DL";
var hoursInAdvanceDictionary = new Dictionary<string, int>
{
    {"AMS", 11},
    {"CUN", 5},
    {"BOG", 5},
    {"MEX", 5},
};
const string Headers = "flight_carrier,flight_number,station,departure,expected,hours_in_advance";

using var stream = new FileStream(FilePath, FileMode.Open);
IWorkbook? workbook = null;

Console.WriteLine($"Starting processing {FilePath} at {DateTime.Now.ToString("s", CultureInfo.InvariantCulture)}");

if (FilePath.ToLower().EndsWith(".xlsx"))
{
    Console.WriteLine("Using new format XSSFWorkbook");
    workbook = new XSSFWorkbook(stream);
}
else
{
    Console.WriteLine("Using old format HSSFWorkbook");
    workbook = new HSSFWorkbook(stream);
}

var sheet = workbook.GetSheetAt(0);
Console.WriteLine($"Started processing sheet {sheet.SheetName} at {DateTime.Now}");

var csvFlights = new List<string>(); 
for (var rowIndex = StartRowIndex; rowIndex <= sheet.LastRowNum; rowIndex++)
{
    var row = sheet.GetRow(rowIndex);
    if (row == null) continue;

    var flightNumber = row.GetCell(Field.FlightNumber.ColumnIndex());
    var departureStation = row.GetCell(Field.DepartureStation.ColumnIndex()).ToString();
    if (departureStation == null)
    {
        Console.WriteLine($"Departure station is null at row: {rowIndex}");
        return;
    }
    var departureTime = row.GetCell(Field.DepartureTime.ColumnIndex()).ToString();
    if (departureTime == null)
    {
        Console.WriteLine($"Departure time is null at row: {rowIndex}");
        return;
    }
    var departureTimeOnly = TimeOnly.ParseExact(departureTime, "HH:mm");
    var hoursInAdvance = hoursInAdvanceDictionary[departureStation];
    var expectedTimeOnly = departureTimeOnly.AddHours(hoursInAdvance);
    
    var effective = row.GetCell(Field.Effective.ColumnIndex()).ToString();
    var effectiveDate = DateOnly.ParseExact(effective, "ddMMMyyyy");
    var dissolution = row.GetCell(Field.Dissolution.ColumnIndex()).ToString();
    var dissolutionDate = DateOnly.ParseExact(dissolution, "ddMMMyyyy");
    for (var i = 0; i <= dissolutionDate.DayNumber - effectiveDate.DayNumber; i++)
    {
        var date = effectiveDate.AddDays(i);
        var departureDateTime = date.ToDateTime(departureTimeOnly);
        var expectedDateTime = date.ToDateTime(expectedTimeOnly);
        var csvFlight = $"{Carrier},{flightNumber},{departureStation},{departureDateTime:u},{expectedDateTime:u},{hoursInAdvance}";
        csvFlights.Add(csvFlight);
    }
}

var outputFileName = $"flights-{DateTime.Now:u}.csv";
using var outputFile = new StreamWriter(outputFileName);
outputFile.WriteLine(Headers);
foreach (var csvFlight in csvFlights)
    outputFile.WriteLine(csvFlight);
Console.WriteLine($"Created file {outputFileName}");

Console.WriteLine($"Finished processing {FilePath} at {DateTime.Now.ToString("s", CultureInfo.InvariantCulture)}");
