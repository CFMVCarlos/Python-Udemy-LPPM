import random
import time

print(time.gmtime(0))

print(time.localtime())

print(time.time())

time_here = time.localtime()
print(time_here)
print(f"Year: {time_here.tm_year}\nMonth: {time_here.tm_mon}\nDay: {time_here.tm_mday}")

input("Press Enter to start the timer")
start_time = time.perf_counter()
input("Press Enter to stop the timer")
end_time = time.perf_counter()

print(f"Started at {time.strftime('%X', time.localtime(start_time))}")
print(f"Ended at {time.strftime('%X', time.localtime(end_time))}")
print(f"Your reaction time was {end_time - start_time} seconds")
