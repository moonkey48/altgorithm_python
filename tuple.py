input_value = input()

splited = input_value.split()
year, month, day = tuple(splited)
print(day + '/' + month + '/' + year)

def read_date():
    year, month, day = tuple(map(int, input().split()))
    return year, month, day

def advanced_day(date):
    year, month, day = date
    
    end_of_month = (month, day) in [(1,31), (2, 28), (3, 31), (4, 30), (5,
        31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
    end_of_year = month == 12 and day == 31
    
    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    print("tommorow done")
    return year, month, day

def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))

if __name__ == "__main__":
    today = read_date()
    print_date(today)
    print("?")
    tommorow = advanced_day(today)
    print(tommorow)
    
    
    
    