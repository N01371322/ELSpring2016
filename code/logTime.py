import datetime
import sqlite3

#this function returns the actual date in the format YYY-MM-DD
def getDate():
	date = "%s-%s-%s" % (datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)
	print date
	return date 
#this function returns the actual time in the format H:M:S
def getTime():
        time = "%s:%s:%s"% (datetime.datetime.today().hour, datetime.datetime.today().minute, datetime.datetime.today().second)
        print time
        return time

#this function access the database testTime and inserts
# a row whith the actual date and time
def logTime():
	conn = sqlite3.connect("testTime.db")
	c = conn.cursor()
	c.execute("INSERT INTO testTime values ('%s', '%s')" % (getDate(), getTime()))
	conn.commit()
	conn.close()
logTime()
	

