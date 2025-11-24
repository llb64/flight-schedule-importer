using FlightScheduleImporter.Enums;

namespace FlightScheduleImporter.Extensions
{
    public static class FieldExtensions
    {
        /// <summary>
        /// Method <c>ColumnIndex</c> multiplies the value of the Field by two, because the import files have an empty column between the fields.
        /// </summary>
        public static int ColumnIndex(this Field field)
            => ((int)field) * 2;
    }
}