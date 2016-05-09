import os
import datetime
import sqlite3


#this function access the file "w1_slave", where the temperature
# is written and split it to get the temperature
def getTemp():
	tempfile = open("/sys/bus/w1/devices/28-0000069757fc/w1_slave") #access the file w1_slave
	tempfile_text = tempfile.read() #copy the text of the file to the variable tempfile_text
	tempfile.close() #close the file
	tempC = int(tempfile_text.split("\n")[1].split("t=")[1]) #get only the number that represents the temperature from the variable and convert it to integer
	return tempC

#this function access the database testTime and inserts
# a row whith the actual date and time
def logTemp():
	conn = sqlite3.connect("tempTable.db") #connect to the database
	c = conn.cursor() #create a cursor
	c.execute("INSERT INTO tempTable values ('%s', '%s')" % (datetime.datetime.today(), getTemp())) #insert the date time and temperature to the database
	conn.commit() #confirm the changes in the table
	conn.close() #close connection to the database
logTemp()
