import datetime
import locale

locale.setlocale(locale.LC_ALL, "")
start: datetime.date = datetime.date(2022, 2, 4)
print(start)

pretty_start: str = start.strftime("%A, %B %d, %Y")
print(pretty_start)

duration = datetime.timedelta(days=15, hours=48)
end: datetime.date = start + duration
print(end)
print(duration)

d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)
print(d1, d2, d3, sep=", ")
print(repr(d1), repr(d2), repr(d3), sep=", ")
