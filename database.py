import MySQLdb
import datetime

day = datetime.datetime.today().weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Open database connection
db = MySQLdb.connect("localhost", "ahmed", "ahmed", "project")
# prepare a cursor object using cursor() method
cursor = db.cursor()


def getDBInfo(label):
    cursor.execute('select username from names where ID="%s";' % label)
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print " \t Hello %s " % data

    cursor.execute('select * from schedule where ID_Name="%s" and day="%s" ;' % (label, days[day]))
    results = cursor.fetchall()
    for row in results:
        st = row[1]
        et = row[2]
        course = row[5]
        room = row[3]
        # Now print fetched result
        print "%s, %s ,%s ,%s" % \
              (st, et, course, room)

    cursor.execute('select * from management where ID_Name="%s" ;' % label)
    result = cursor.fetchall()
    for row in result:
        print row


def close():
    # disconnect from server
    db.close()
