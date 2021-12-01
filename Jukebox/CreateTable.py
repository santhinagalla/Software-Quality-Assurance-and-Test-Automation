import pymysql

db = pymysql.connect(host="HostName",user="root",passwd="123456789",database="db")
# Prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to Create a songList table into the database.
sql ="CREATE TABLE songList(songName varchar(32), creditCardNum varchar(32))"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    # disconnect from server
db.close()