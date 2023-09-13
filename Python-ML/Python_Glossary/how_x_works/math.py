def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("true")
    else:
        print("false")

leapYear(1992)