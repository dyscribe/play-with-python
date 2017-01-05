# Views the current content of a database table

# Importing Libs
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","python_app","py99","hyperion" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM pythonApp;"

try:
    # run the sql
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
      releaseNumber = row[0]
      title = row[1]
      genre = row[2]
      # Now print fetched result
      print "%s. %s | %s" % \
             (releaseNumber, title, genre )
except:
    print "Error: did not work."

# execute SQL query using execute() method.
# data = cursor.execute("SELECT * FROM pythonApp;")

# Fetch a single row using fetchone() method.
#print "Current Table Contents are : %s " % data

# disconnect from server
db.close()
