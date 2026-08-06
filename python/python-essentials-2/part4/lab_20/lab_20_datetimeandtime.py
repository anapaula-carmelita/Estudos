from datetime import datetime

def format_date(year, month, day, hour, minute, second):
    d = datetime(year, month, day, hour, minute, second)

    print(d.strftime("%Y/%m/%d %H:%M:%S")) #2020/11/04 14:53:00
    print(d.strftime("%y/%B/%d %H:%M:%S %p")) #20/November/04 14:53:00 PM

    print(d.strftime("%a, %Y %b %d")) #Wed, 2020 Nov 04
    print(d.strftime("%A, %Y %B %d")) #Wednesday, 2020 November 04
    print(f"Weekday: {d.strftime('%w')}") # Weekday: 3
    print(f"Day of the year: {d.strftime('%j')}")# Day of the year: 309
    print(f"Week number of the year: {d.strftime('%U')}") # Week number of the year: 44

if __name__ == "__main__":
    format_date(2020, 11, 4, 14, 53, 00)