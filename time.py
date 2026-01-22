from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta

tz = pytz.timezone("Asia/Tashkent")

# Hozirgi vaqt (datetime)
now_dt = datetime.now(tz)
# print("Hozir:", now_dt)

# 1 oy qo‘shish
next_month = now_dt + relativedelta(months=1)
# print("1 oy keyin:", next_month)

# Timestamp shaklida
next_month_ts = int(next_month.timestamp())
# print("Timestamp:", next_month_ts)


# timestamp → Toshkent vaqti
ts = 1803754800
dt = datetime.fromtimestamp(ts, tz)
# print(dt)

formatted = next_month.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)

date_str = "21.02.2026 22:22"
dt = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
print(dt)


