import pymysql
# Open database connection
db = pymysql.connect(host="HostName",user="root",passwd="123456789",database="db")
# Prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM songList;"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        songName = row[0]
        creditCardNum = row[1]
        # Now print fetched result
        print ("songName = %s, Credit Card Number = %s" % (songName, creditCardNum))
except:
    print ("Error: unable to fetch data")
# disconnect from server
db.close()