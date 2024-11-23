from datetime import date, time

meeting = time(hour=11, minute=15, second=0)
print(meeting)

end_time = time(hour=12, minute=30)
print(end_time)

#! Not Allowed
# meeting_duration = end_time - meeting
# print(meeting_duration)

iso_time = "11:15:00"
_time: time = time.fromisoformat(iso_time)
print(_time)
