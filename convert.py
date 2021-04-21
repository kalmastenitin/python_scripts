import datetime, pytz
from datetime import timezone

local_tz = pytz.timezone("Asia/Kolkata")

date = input("Enter date in format 2021-04-21 10:12: ")
d = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
print("Given datetime: ",d)
e = local_tz.localize(d, is_dst=None)
print("Localized datetime: ",e)
m = e.astimezone(pytz.utc)
print("UTC datetime: ",m)