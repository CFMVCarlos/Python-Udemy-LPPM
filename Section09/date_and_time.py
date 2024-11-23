import datetime
import time

print(f"The epoch on this system starts at {time.strftime('%c', time.gmtime(0))}")
print(
    f"The current timezone is {time.tzname[0]} with an offset of {time.timezone} seconds"
)

if time.daylight != 0:
    print(f"\tDaylight Saving Time is in effect for this location")
    print(f"\tThe DST timezone is {time.tzname[1]}")

print(f"Local time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
print(f"UTC time is {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")

########################################################################################
print("\n" + "=" * 100 + "\n")
########################################################################################

print(datetime.datetime.today())
print(datetime.datetime.now())
