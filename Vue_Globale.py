import datetime

class Date :

    def ConversionDate(year, day, month):
        date_obj = datetime.datetime(year=year, month=month, day=day)
        day_of_year = date_obj.timetuple().tm_yday

        return day_of_year



