###   Dates  ###

from datetime import datetime

now = datetime.now()
print(f'Año: {now.year}')
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestap = now.timestamp()
print(timestap)

year_2023 = datetime(2024, 1, 24)
def print_date(self):
    print(f'La fecha guardada es: {year_2023}')

print_date(year_2023)


from datetime import time

current_time = time(22, 1, 0)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_day = date(2023, 1, 24)
print(current_day)
print(current_day.year)
print(current_day.month)
print(current_day.day)

current_day = date.today()
print(current_day)
print(current_day.year)
print(current_day.month)
print(current_day.day)


current_day = date(current_day.year, current_day.month + 3, current_day.day)
print(current_day)

print(f'year_2023: {year_2023}')
print(f'now: {now}')
print(year_2023 - now)

print(f'year_2023: {year_2023}')
print(f'current_day: {current_day}')
print(year_2023.date() - current_day)


from datetime import timedelta
init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=30)
print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)
print(init_timedelta)
print(end_timedelta)

