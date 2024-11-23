import datetime

import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.now(datetime.timezone.utc)

print(f"Naive local time: {local_time}")
print(f"Aware UTC time: {utc_time}")

print()

aware_local_time = pytz.utc.localize(local_time)

print(f"Aware local time: {aware_local_time}, {aware_local_time.tzinfo}")
print(f"Aware UTC time: {utc_time}, {utc_time.tzinfo}")

print()

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

