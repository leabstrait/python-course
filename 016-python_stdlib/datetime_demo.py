import datetime

# Date
tday = datetime.date(2020, 1, 15)
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())

# Time differences
tdelta = datetime.timedelta(days=30)
print(tday-tdelta)

# Birthday
bday = datetime.date(2020, 12, 28)
tillbday = bday - tday
print(tillbday)

# Time
t = datetime.time(3, 34, 23, 5000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# DateTime
dt = datetime.datetime(2020, 1 ,15, 3, 34, 23, 5000)
print(dt)
print(dt.date())
print(dt.time())

# Delta
print(dt+tdelta)

# DateTime at this point
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# Formatting Date and Time
print(dt_now.strftime('%m %d, %Y'))

date_str = 'December 28, 1993'
bday = datetime.datetime.strptime(date_str, '%B %d, %Y')
print(bday)

