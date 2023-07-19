# importing modules
import datetime
import calendar
# defining function as calender_program

def calender_program(year,month,date):
    # using datetime module date constructor is created
    # date object is created and 3 arguments: year,month,date is passed
    input_date = datetime.date(year, month, date)
    #day_name is an array that contains the days and week in that particular month
    # this is imported from calender module and stored in the result variable
    result = calendar.day_name[input_date.weekday()].upper()
    # prints the result
    print(result)
    # returns the result
    return result


