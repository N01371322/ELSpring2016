import datetime
import sqlite3

conn = sqlite3.connect('testTime.db')

c = conn.cursor()

date = datetime.datetime.today()
day = date.day
month = date.month
year = date.year
hour = date.hour
minute = date.minute
second = date.second

day = "%s-%s-%s" % (year, month, day)
hour = "%s:%s:%s" % (hour, minute, second)

c.execute("insert into testTime values ('%s', '%s')" % (day, hour))
conn.commit()
conn.close()
print day, hour

