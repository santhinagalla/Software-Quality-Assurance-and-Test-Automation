#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
import sys
sys.path.append('/home/sans/.local/lib/python3.9/site-packages')
import pymysql, requests, json
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
song = form.getvalue('song')
creditCardNum = form.getvalue('creditCardNum')
captchaResponse = form.getvalue('g-recaptcha-response')

def is_human(captcha_response):
    """ Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.
    """
    secret = "Generate key and paste here"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']
if True: #is_human(captchaResponse):
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<h2>Hello %s %s</h2>" % (song, creditCardNum))
    print("</body>")
    print("</html>")
    
    db = pymysql.connect(host="HostName",user="root",passwd="123456789",database="db")
    # Prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO songList(songName, creditCardNum) VALUES (%s,%s)"
    try:
        # Execute the SQL command
        cursor.execute(sql,(song, creditCardNum))
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    # disconnect from server
    db.close()
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    #print("<head>")
    #print("<title>Hello - Second CGI Program</title>")
    #print("</head>")
    print("<body>")
    print("<h2>I am a ROBOT </h2>")
    print("</body>")
    print("</html>")