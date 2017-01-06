# Executing an SQL query that displays data from a local MySQL test-database

# Importing Libs
import MySQLdb

# Connect to a local MySQL database
# Don't get too excited, these are just test credentials
db = MySQLdb.connect("localhost","python_app","py99","hyperion" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to SELECT data from the test-table
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

# disconnect from the database
db.close()
