import calendar  


def count_weekday_in_year(year, weekday):
    c = calendar.Calendar()
    count = 0
    for month in range(1, 13):
        for data in c.monthdays2calendar(year, month):
            if data[weekday][0] != 0:
                count += 1

    return count

if __name__ == "__main__":
    print(count_weekday_in_year(2019, 0))
    print(count_weekday_in_year(2000, 6))