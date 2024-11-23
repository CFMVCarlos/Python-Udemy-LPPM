import datetime
import time

import pytz

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print(f"The time in {country} is {local_time}")
print(f"UTC is {datetime.datetime.now(tz=pytz.timezone("UTC"))}")

# for x in pytz.all_timezones:
#     print(x)

for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}", end=": ")
    if x in pytz.country_timezones:
        for zone in pytz.country_timezones[x]:
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f"\t\t{zone}: {local_time}", end=": ")
    else:
        print("\t\tNo timezone defined")
